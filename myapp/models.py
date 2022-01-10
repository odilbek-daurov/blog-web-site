from django.contrib.auth.models import User
from django.db import models
from taggit.managers import TaggableManager


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='bo`lim nomi')
    slug = models.SlugField(max_length=100,unique=True)
    
    def __str__(self) -> str:
        return self.name
    
    
class Blog(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255,unique=True)
    image = models.ImageField(upload_to = 'blog/%Y/%m/%d')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='bolim')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = TaggableManager()
    
    def __str__(self) -> str:
        return self.title
    
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    text = models.TextField()
    