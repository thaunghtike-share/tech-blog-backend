from rest_framework import serializers
from .models import Category, Tag, Author, Article, Comment

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

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

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'name', 'content', 'created_at']
        read_only_fields = ['id', 'created_at']

    def validate(self, attrs):
        # Set a default name if missing
        if not attrs.get('name'):
            attrs['name'] = 'Anonymous'
        return attrs
