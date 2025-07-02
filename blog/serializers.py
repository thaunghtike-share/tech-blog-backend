from rest_framework import serializers
from .models import Category, Tag, Author, Article

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
        fields = ['id', 'name', 'bio', 'avatar']

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