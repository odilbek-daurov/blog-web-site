from django.urls import path

from .views import blog_list,category_blog

urlpatterns = [
    path('',blog_list, name='blog_list'),
    path('category/<slug:slug>', category_blog,name='category_blog')
]
