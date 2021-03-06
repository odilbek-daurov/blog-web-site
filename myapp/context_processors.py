from taggit.views import Tag
from .models import Blog, Category

def category(request):
    categories = Category.objects.all()
    return {'categories':categories}


def tags(request):
    tags = Tag.objects.all()
    return {'tags':tags}


def views_last(request):
    last = Blog.objects.order_by('-views')
    return { 'last':last }