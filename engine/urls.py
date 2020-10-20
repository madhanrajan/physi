from django.urls import path, include
from .views import PostDetailView, PostListView, BookCreateView, SpecificPostList, Index, BookList, BookDetail, PostCreateView, TagCreateView, FeedbackView

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('post_list', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('book_create', BookCreateView.as_view(), name='book_create'),
    path('book/<int:book_pk>/post_list', SpecificPostList.as_view(),
         name='specific_post_list'),
    path('book_list', BookList.as_view(), name='user_books'),
    path('book/<int:pk>', BookDetail.as_view(), name='book_detail'),
    path('book/<int:book_pk>/post_create',
         PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/create_tag',
         TagCreateView.as_view(), name='post_tag_create'),
    path('feedback/', FeedbackView.as_view(), name='feedback'),

]
