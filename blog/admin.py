from django.contrib import admin
from .models import Category, Tag, Author, Article, MMPlaylist

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Author)
admin.site.register(Article)
admin.site.register(MMPlaylist)
