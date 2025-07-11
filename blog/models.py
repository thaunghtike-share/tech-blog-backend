from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# create category model
class Category(models.Model):   
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# create tag model
class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name   

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="author_profile")
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    avatar = models.URLField(blank=True)
    featured = models.BooleanField(default=False)
    job_title = models.CharField(max_length=100, blank=True)
    company = models.CharField(max_length=100, blank=True)
    linkedin = models.URLField(blank=True)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)
    featured = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title   

class MMPlaylist(models.Model):
    title = models.CharField(max_length=255)
    video_id = models.CharField(max_length=32)
    playlist_url = models.URLField()
    duration = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class FreeLab(models.Model):
    title = models.CharField(max_length=255)
    platform = models.CharField(max_length=100)
    url = models.URLField()
    description = models.TextField()
    difficulty = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.title   

class Playlist(models.Model):
    title = models.CharField(max_length=255)
    video_id = models.CharField(max_length=50)  # YouTube video ID for embed
    playlist_url = models.URLField()
    channel = models.CharField(max_length=100, blank=True)  # Channel name
    difficulty = models.CharField(max_length=20, blank=True)  # e.g., Beginner, Intermediate
    duration = models.CharField(max_length=50, blank=True)  # Estimated duration like "3-5 weeks"

    def __str__(self):
        return self.title             

