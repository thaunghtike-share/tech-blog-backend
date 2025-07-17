from rest_framework import serializers
from .models import Category, Tag, Author, Article, MMPlaylist, FreeLab, Playlist, Project, UdemyCourse, Testimonial

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

from .models import Testimonial

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = ['id', 'name', 'role', 'feedback', 'rating', 'created_at']
        read_only_fields = ['id', 'created_at']

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = [
            'id',
            'name',
            'bio',
            'avatar',
            'featured',
            'job_title',
            'company',
            'linkedin'  # New field for LinkedIn URL
        ]

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = [
            'id', 'title', 'content', 'published_at',
            'category',  # Accepts category ID
            'tags',      # Accepts list of tag IDs
            'author',    # Read-only if you want
            'featured',
            'read_count',
            'slug'
        ]
        read_only_fields = ['author']

class ArticleTopReadSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source="author.name", default="Unknown", read_only=True)

    class Meta:
        model = Article
        fields = ["id", "slug", "title", "published_at", "author_name", "read_count"]        

class FreeLabSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreeLab
        fields = '__all__'      

class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = [
            "id",
            "title",
            "video_id",
            "playlist_url",
            "channel",
            "difficulty",
            "is_burmese",
            "duration",
        ]   

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'url', 'tags']     

class UdemyCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = UdemyCourse
        fields = ['id', 'title', 'description', 'url', 'author', 'author_image', 'rating']          