from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, TemplateView, FormView
from engine.models import Topic, Book
from django.urls import reverse
from .forms import TopicForm, BookForm, TagForm
from django.shortcuts import render_to_response
import os
from .documents import TopicDocument
import uuid
from urlcreator.models import PDFRetriever
from feedback.forms import FeedbackForm
from feedback.models import FeedbackData

class PostListView(ListView):
    model = Topic
    template_name = 'engine/post_list.html'

    def get_queryset(self):
        q = self.request.GET.get('q', '')
        if q.replace(" ", "") == "":
            return Topic.objects.all()
        else:
            return TopicDocument.search().query("multi_match", query=q, fields=["title", "document"]).to_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query_text"] = self.request.GET.get("q", '')
        return context


class PostDetailView(DetailView):
    model = Topic
    template_name = 'engine/post_detail.html'

    def dispatch(self, *args, **kwargs):
        dispatch_method = super(PostDetailView, self).dispatch


        return dispatch_method(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        instance_url = Topic.objects.get(pk=self.kwargs.get('pk')).document.url
        id = str(uuid.uuid4())
        PDFRetriever.objects.create(token=id, pdf_url=instance_url)

        uri = "https://cors-anywhere.herokuapp.com/" + 'https://www.physi.co.uk/short/' + id

        context["data"] = uri
        

        return context


class PostCreateView(FormView):
    template_name = 'engine/post_create.html'
    form_class = TopicForm

    def get_success_url(self):
        return reverse('specific_post_list', kwargs={"book_pk": self.kwargs.get('book_pk')})

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        file_list = request.FILES.getlist('file_field')
        book = Book.objects.get(pk=kwargs["book_pk"])

        if form.is_valid():
            for f in file_list:
                filename = os.path.splitext(f.name)[0]
                Topic.objects.create(
                    title=filename, source_file=book, document=f,)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class BookCreateView(CreateView):
    template_name = 'engine/book_create.html'
    form_class = BookForm

    def get_success_url(self):
        return reverse('user_books')


class BookList(ListView):
    template_name = 'engine/book_list.html'

    def get_queryset(self):
        return Book.objects.all()


class BookDetail(DetailView):
    model = Book
    template_name = 'engine/book_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        instance_url = Book.objects.get(pk=self.kwargs.get('pk')).document.url
        id = str(uuid.uuid4())
        PDFRetriever.objects.create(token=id, pdf_url=instance_url)

        url = "https://cors-anywhere.herokuapp.com/" + 'https://www.physi.co.uk/short/' + id

        context["data"] = url

        return context


class SpecificPostList(ListView):
    model = Topic
    template_name = 'engine/specific_post_list.html'

    def get_queryset(self):
        book = Book.objects.get(pk=self.kwargs.get('book_pk'))
        queryset = Topic.objects.filter(source_file=book)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["book_pk"] = self.kwargs.get('book_pk')

        return context


class Index(FormView):
    template_name = 'engine/index.html'
    form_class = FeedbackForm

    def form_valid(self, form):
        data = form.cleaned_data["data"]

        inst = FeedbackData.objects.create(data=data)
        inst.save()

        return super().form_valid(form)

    def save(self, commit=True):
        instance = super().save(commit=False)

        return instance

    def get_success_url(self):
        return reverse("feedback")



class TagCreateView(FormView):
    form_class = TagForm
    template_name = 'engine/post_tag_create.html'

    def get_success_url(self):
        return reverse('post_list')

    def form_valid(self, form):
        tag_list = form.cleaned_data["tags"]
        post = Topic.objects.get(pk=self.kwargs.get('pk'))

        post.add_tags(tag_list)

        return super().form_valid(form)

class FeedbackView(TemplateView):
    template_name = 'engine/feedback.html'

class ConstructionView(TemplateView):
    template_name = 'engine/construction.html'