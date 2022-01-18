from django.urls import path

from .views import ( blog_create, blog_list, blog_updete,category_blog,
                    category_list, blog_detail, tag_list )

urlpatterns = [
    path('',blog_list, name='blog_list'),
    path('blog/<slug:slug>', blog_detail, name='blog_detail'),
    path('category', category_list,name='category_list'),
    path('category/<slug:slug>', category_blog,name='category_blog'),
    path('tag/<slug:slug>', tag_list, name="tag_list"),
    path('create/', blog_create, name="blog_create"),
    path('updete/<slug:slug>', blog_updete, name="blog_updete")


    
]
