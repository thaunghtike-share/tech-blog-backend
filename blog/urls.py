from django.urls import path
from .views import *
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('categories/', CategoryListCreateAPIView.as_view(), name='category-list-create'),
    path('categories/<int:id>/', CategoryRetrieveUpdateDestroyAPIView.as_view(), name='category-detail'),
    path('categories/<int:id>/stats/', CategoryStatsAPIView.as_view(), name='category-stats'),

    path('tags/', TagListCreateAPIView.as_view(), name='tag-list-create'),
    path('tags/<int:id>/', TagRetrieveUpdateDestroyAPIView.as_view(), name='tag-detail'),

    path('authors/', AuthorListCreateAPIView.as_view(), name='author-list-create'),
    path('authors/<int:id>/', AuthorRetrieveUpdateDestroyAPIView.as_view(), name='author-detail'),

    path('articles/', ArticleListCreateAPIView.as_view(), name='article-create'),
    path('articles/<int:id>/', ArticleRetrieveUpdateDestroyAPIView.as_view(), name='article-detail'),
    path('articles/stats/', ArticleStatsAPIView.as_view(), name='article-stats'),

    path('login/', obtain_auth_token, name='api_token_auth'),
]