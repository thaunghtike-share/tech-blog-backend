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

# create author model
class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    avatar = models.URLField(blank=True)
    featured = models.BooleanField(default=False)  
    job_title = models.CharField(max_length=100, blank=True)
    company = models.CharField(max_length=100, blank=True)
    linkedin = models.URLField(blank=True)  # New field for LinkedIn URL

    def __str__(self):
        return self.name    
          

# create article model
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

# comments        
class Comment(models.Model):
    article = models.ForeignKey("Article", on_delete=models.CASCADE, related_name="comments")
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE, related_name="replies")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")  # NEW
    name = models.CharField(max_length=100)
    content = models.TextField()
    rating = models.PositiveSmallIntegerField(null=True, blank=True)
    image = models.ImageField(upload_to="comment_images/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username if self.user else self.name} on article {self.article_id}"
