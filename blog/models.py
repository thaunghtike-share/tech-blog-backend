from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify

User = get_user_model()

# create category model
class Category(models.Model):   
    name = models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True, unique=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

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
    slug = models.SlugField(null=True, blank=True, unique=True)

    read_count = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            existing_slugs = Article.objects.values_list("slug", flat=True)
            slug = base_slug
            counter = 1
            while slug in existing_slugs:
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def increment_read_count(self):
        self.read_count += 1
        self.save(update_fields=["read_count"])

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
    is_burmese = models.BooleanField(default=False)  # new field added
    channel = models.CharField(max_length=100, blank=True)  # Channel name
    difficulty = models.CharField(max_length=20, blank=True)  # e.g., Beginner, Intermediate
    duration = models.CharField(max_length=50, blank=True)  # Estimated duration like "3-5 weeks"

    def __str__(self):
        return self.title   

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    url = models.URLField()
    tags = models.JSONField(default=list)  # stores list of tags

    def __str__(self):
        return self.name     

class UdemyCourse(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    url = models.URLField()
    author = models.CharField(max_length=255)
    rating = models.FloatField(blank=True, null=True)
    author_image = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title             

