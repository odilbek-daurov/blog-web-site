from taggit.views import Tag
from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog, Category
from .forms import BlogForm



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
       "blogs":blog,
    }
    
    return render(request, 'category_blog.html', context)


def category_list(reques):
    categories = Category.objects.all()
    
    context = {
        'categories':categories,
    }
    return render(reques,'category_list.html',context)

def blog_detail(request, slug):
    blog = get_object_or_404( Blog, slug=slug)
    blog.views += 1
    blog.save()
    context = {
        "blog":blog,
    }
    
    return render(request,"blog_detail.html",context)

def tag_list(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    blogs = Blog.objects.filter(tags=tag)
    
    context = {
        "blogs":blogs,
        'tag':tag,
    }
    return render(request,'home.html',context)


def blog_create(request):
    form = BlogForm()
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
        
    context = {
        'form':form
    }

    return render(request, 'blog_create.html', context)
    
