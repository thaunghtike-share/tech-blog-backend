from rest_framework import serializers
from .models import Category, Tag, Author, Article, MMPlaylist, FreeLab, Playlist

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class MMPlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = MMPlaylist
        fields = '__all__'

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
            'featured'
        ]
        read_only_fields = ['author']

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
            "duration",
        ]          