from rest_framework import serializers
from .models import (
    Category, Tag, Author, Article, MMPlaylist, FreeLab,
    Playlist, Project, UdemyCourse, Testimonial
)

class CategorySerializer(serializers.ModelSerializer):
    post_count = serializers.IntegerField(read_only=True)
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'post_count']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'slug', 'name']

class MMPlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = MMPlaylist
        fields = '__all__'

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = ['id', 'name', 'role', 'feedback', 'rating', 'created_at']
        read_only_fields = ['id', 'created_at']

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = [
            'id', 'name', 'bio', 'avatar', 'featured', 'slug',
            'job_title', 'company', 'linkedin'
        ]

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = [
            'id', 'title', 'content', 'published_at',
            'category', 'tags', 'author', 'featured',
            'read_count', 'slug'
        ]
        read_only_fields = ['author']

class ArticleTopReadSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source="author.name", default="Unknown", read_only=True)

    class Meta:
        model = Article
        fields = [
            "id", "slug", "title", "published_at",
            "author_name", "read_count"
        ]

class ArticleExcerptSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source="author.name", default="Unknown", read_only=True)
    excerpt = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = [
            "id", "slug", "title", "published_at",
            "author_name", "read_count", "excerpt"
        ]

    def get_excerpt(self, obj):
        raw = obj.content or ""
        excerpt = raw[:250] + "..." if len(raw) > 250 else raw
        return excerpt

# Distinct serializer class names for clarity and to avoid import errors
class AuthorWithArticlesExcerptSerializer(serializers.ModelSerializer):
    articles = ArticleExcerptSerializer(source='article_set', many=True)

    class Meta:
        model = Author
        fields = [
            'id', 'name', 'slug', 'bio', 'avatar',
            'job_title', 'company', 'linkedin', 'featured',
            'articles'
        ]

class AuthorWithArticlesTopReadSerializer(serializers.ModelSerializer):
    articles = ArticleTopReadSerializer(source='article_set', many=True)

    class Meta:
        model = Author
        fields = [
            'id', 'name', 'slug', 'bio', 'avatar',
            'job_title', 'company', 'linkedin', 'featured',
            'articles'
        ]

class FreeLabSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreeLab
        fields = '__all__'

class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = [
            "id", "title", "video_id", "playlist_url",
            "channel", "difficulty", "is_burmese", "duration",
        ]

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'url', 'tags']

class UdemyCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = UdemyCourse
        fields = ['id', 'title', 'description', 'url', 'author', 'author_image', 'rating']
