from django import forms
from .models import Topic, Book


class TopicForm(forms.Form):
    file_field = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'multiple': True}))


class TagForm(forms.Form):
    tags = forms.CharField(max_length=200)


class BookForm(forms.ModelForm):

    title = forms.CharField(max_length=200)

    class Meta:
        model = Book
        fields = ["title", "description", "subject", "document"]
