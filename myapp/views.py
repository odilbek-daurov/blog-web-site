from taggit.views import Tag
from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from .models import Blog, Category,Comment
from .forms import BlogForm, CommetForm
from django.template.defaultfilters import slugify
from django.core.paginator import Paginator, EmptyPage



def blog_list(request):
    blog = Blog.objects.all()
    blogs_top = Blog.objects.order_by('-views')[:5]
    
    paginator = Paginator(blog, 2)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page_number)
    except EmptyPage:
        page_obj = paginator.page(1)
    context = {
        "blogs":page_obj,
        'blogs_top':blogs_top,
    }
    return render(request, 'home.html',context)


def category_blog(request, slug):
    category = Category.objects.get(slug = slug)
    blog = Blog.objects.filter(category = category)[:5]
    
    context = {
        "category":category,
       "blogs":blog,
    }
    
    return render(request, 'category_blog.html', context)


def category_list(reques):
    categories = Category.objects.all()
    blogs_top = Blog.objects.order_by('-views')[:5]
    
    context = {
        'blogs_top':blogs_top,
        'categories':categories,
    }
    return render(reques,'category_list.html',context)

def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    top_blogs = Blog.objects.filter(category = blog.category )
    comment = Comment.objects.filter(blog = blog)
    
    blog.views += 1
    blog.save()
    
    if request.method == "POST":
        form = CommetForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.blog = blog
            form.save()
            return redirect('blog_detail', blog.slug) 
    else:
        form = CommetForm()
        
    context = {
        "blog":blog,
        'top_blogs':top_blogs,
        'form':form,
        "comment":comment,
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
            form_date = form.save(commit=False)
            form_date.user = request.user
            form.slug = slugify(form_date.title)
            form_date.save()
            form.save_m2m()
            return redirect('blog_list')
        
    context = {
        'form':form
    }

    return render(request, 'blog_create.html', context)
    

def blog_updete(request, slug):
    blog = Blog.objects.get(slug = slug)
    form = BlogForm(instance=blog)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form_date = form.save(commit=False)
            form_date.user = request.user
            form.slug = slugify(form_date.title)
            form_date.save()
            form.save_m2m()
            return redirect('blog_list')
        
    context = {
        'form':form
    }

    return render(request, 'blog_updete.html', context)
    

def blog_delete(request, slug):
    blog = get_object_or_404(Blog, slug = slug)
    if request.method == 'POST':
        blog.delete()
        return redirect('blog_list')

    context = {
        'blog':blog
    }
    
    return render(request, 'blog_delete.html', context)