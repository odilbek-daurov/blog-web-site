from django.shortcuts import render
from .models import Blog, Category



def blog_list(request):
    blog = Blog.objects.all()
    context = {
        "blogs":blog
    }
    return render(request,'home.html',context)

def category_blog(request, slug):
    category = Category.objects.get(slug = slug)
    blog = Blog.objects.filter(category = category)
    
    context = {
        "category":category,
       " blogs":blog
    }
    
    return render(request, 'category_blog.html', context)