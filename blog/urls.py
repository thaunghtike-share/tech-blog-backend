from django.urls import path
from .views import *

urlpatterns = [
    path('categories/', CategoryListCreateAPIView.as_view(), name='category-list-create'),
    path('categories/<int:id>/', CategoryRetrieveUpdateDestroyAPIView.as_view(), name='category-detail'),

    path('tags/', TagListCreateAPIView.as_view(), name='tag-list-create'),
    path('tags/<int:id>/', TagRetrieveUpdateDestroyAPIView.as_view(), name='tag-detail'),

    path('authors/', AuthorListCreateAPIView.as_view(), name='author-list-create'),
    path('authors/<int:id>/', AuthorRetrieveUpdateDestroyAPIView.as_view(), name='author-detail'),

    path('articles/', ArticleListCreateAPIView.as_view(), name='article-create'),
    path('articles/<int:id>/', ArticleRetrieveUpdateDestroyAPIView.as_view(), name='article-detail'),
]