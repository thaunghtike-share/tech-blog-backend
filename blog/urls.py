from django.urls import path
from . import views
from .views import *
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('categories/', CategoryListCreateAPIView.as_view(), name='category-list-create'),
    path('categories/<int:id>/stats/', CategoryStatsAPIView.as_view(), name='category-stats'),

    path('tags/', TagListCreateAPIView.as_view(), name='tag-list-create'),
    path('tags/<int:id>/', TagRetrieveUpdateDestroyAPIView.as_view(), name='tag-detail'),

    path('authors/', AuthorListCreateAPIView.as_view(), name='author-list-create'),
    path('authors/<int:id>/', AuthorRetrieveUpdateDestroyAPIView.as_view(), name='author-detail'),

    path('articles/', ArticleListCreateAPIView.as_view(), name='article-create'),
    path('articles/stats/', ArticleStatsAPIView.as_view(), name='article-stats'),

    path('login/', obtain_auth_token, name='api_token_auth'),
    path('mmplaylists/', MMPlaylistListView.as_view(), name="mmplaylist-list"),

    path('articles/<int:id>/read/', ArticleReadAPIView.as_view(), name='article-read'),
    path("articles/<int:pk>/increment-read/", views.increment_read_count),
    path("articles/top-read/", TopReadArticlesView.as_view(), name="top-read-articles"),

    path('freelabs/', FreeLabListAPIView.as_view(), name="freelab-list"),
    path('playlists/', PlaylistListView.as_view(), name='playlist-list'),
    path('projects/', ProjectListAPIView.as_view(), name='project-list'),
    path('udemy-courses/', UdemyCourseList.as_view(), name='udemy-course-list'),

    path('articles/<slug:slug>/', ArticleRetrieveUpdateDestroyAPIView.as_view(), name='article-detail'),
    path('categories/<slug:slug>/', CategoryRetrieveUpdateDestroyAPIView.as_view(), name='category-detail'),
]