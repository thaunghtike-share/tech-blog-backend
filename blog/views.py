from rest_framework import generics, permissions, status
from rest_framework.filters import SearchFilter
from .models import Category, Tag, Author, Article, MMPlaylist, FreeLab, Playlist, Project, UdemyCourse
from .serializers import CategorySerializer, TagSerializer, AuthorSerializer, ArticleSerializer, MMPlaylistSerializer, ArticleTopReadSerializer, FreeLabSerializer, PlaylistSerializer, ProjectSerializer, UdemyCourseSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from django.db.models import Count
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.decorators import api_view, permission_classes

class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny] 

    def get_queryset(self):
        return Category.objects.annotate(post_count=Count('article'))
    
class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'slug'

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
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # ✅ Require login

    def get_queryset(self):
        queryset = Author.objects.all()
        featured = self.request.query_params.get('featured')
        if featured is not None:
            if featured.lower() in ['true', '1', 'yes']:
                queryset = queryset.filter(featured=True)
            elif featured.lower() in ['false', '0', 'no']:
                queryset = queryset.filter(featured=False)
        return queryset

class AuthorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'id'

class ArticleListCreateAPIView(generics.ListCreateAPIView):
    queryset = Article.objects.all().order_by('-published_at')
    serializer_class = ArticleSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['category', 'category__slug', 'author', 'tags', 'featured']  # ✅ Add this
    search_fields = ['title', 'content']
    permission_classes = [IsAuthenticatedOrReadOnly]  # ✅ Require login

    def perform_create(self, serializer):
        try:
            author = self.request.user.author_profile  # ✅ Get linked author
        except Author.DoesNotExist:
            raise ValidationError("You are not linked to an Author profile.")

        serializer.save(author=author)

class ArticleRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'slug' 

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

class ArticleReadAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, id, format=None):
        try:
            article = Article.objects.get(id=id)
        except Article.DoesNotExist:
            return Response({"error": "Article not found"}, status=status.HTTP_404_NOT_FOUND)

        article.increment_read_count()

        return Response({
            "message": "Read count incremented.",
            "article_id": article.id,
            "read_count": article.read_count
        }, status=status.HTTP_200_OK)        

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

class MMPlaylistListView(generics.ListAPIView):
    queryset = MMPlaylist.objects.all()
    serializer_class = MMPlaylistSerializer    
    permission_classes = [IsAuthenticatedOrReadOnly]  

class FreeLabListAPIView(generics.ListAPIView):
    queryset = FreeLab.objects.all()
    serializer_class = FreeLabSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]          

class PlaylistListView(generics.ListAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  


class ProjectListAPIView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer       
    permission_classes = [IsAuthenticatedOrReadOnly]

class UdemyCourseList(generics.ListAPIView):
    queryset = UdemyCourse.objects.all()
    serializer_class = UdemyCourseSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

@api_view(['POST'])
@permission_classes([AllowAny])  # ← allow unauthenticated users
def increment_read_count(request, pk):
    try:
        article = Article.objects.get(pk=pk)
        article.read_count += 1
        article.save()
        return Response({'message': 'Read count incremented.'}, status=status.HTTP_200_OK)
    except Article.DoesNotExist:
        return Response({'error': 'Article not found.'}, status=status.HTTP_404_NOT_FOUND)  

class TopReadArticlesView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]  

    def get(self, request):
        limit = int(request.query_params.get("limit", 7))
        articles = Article.objects.order_by("-read_count")[:limit]
        serializer = ArticleTopReadSerializer(articles, many=True)
        return Response(serializer.data)
