from django.db import models

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