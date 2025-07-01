from django.urls import path
from .views import *

urlpatterns = [
    path('categories/', CategoryListAPIView.as_view()),
    path('tags/', TagListAPIView.as_view()),
    path('authors/', AuthorListAPIView.as_view()),
    path('articles/', ArticleListAPIView.as_view()),
    path('articles/<int:id>/', ArticleDetailAPIView.as_view()),
]