from rest_framework import generics, permissions, status
from rest_framework.filters import SearchFilter
from .models import Category, Tag, Author, Article
from .serializers import CategorySerializer, TagSerializer, AuthorSerializer, ArticleSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from django.db.models import Count
from rest_framework.response import Response

class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny] 
    
class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'id'

class TagListCreateAPIView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.AllowAny]

class TagRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'id'

class AuthorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.AllowAny]

class AuthorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'id'

class ArticleListCreateAPIView(generics.ListCreateAPIView):
    queryset = Article.objects.all().order_by('-published_at')
    serializer_class = ArticleSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['category', 'author', 'tags', 'featured']
    search_fields = ['title', 'content']
    permission_classes = [permissions.AllowAny]  # only admin can create

class ArticleRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'id'

class ArticleStatsAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        total_articles = Article.objects.count()

        popular_tags = Tag.objects.annotate(article_count=Count('article')).order_by('-article_count')[:5]
        popular_tags_data = [
            {"id": tag.id, "name": tag.name, "count": tag.article_count}
            for tag in popular_tags
        ]

        return Response({
            "total_articles": total_articles,
            "popular_tags": popular_tags_data
        })  

class CategoryStatsAPIView(APIView):
    def get(self, request, id):
        try:
            category = Category.objects.get(id=id)
        except Category.DoesNotExist:
            return Response({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND)

        article_count = Article.objects.filter(category=category).count()
        return Response({
            "category": {
                "id": category.id,
                "name": category.name,
                "article_count": article_count
            }
        })          

