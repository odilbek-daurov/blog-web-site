from django.contrib import admin
from django.contrib.admin.helpers import checkbox
from django.db import models
from .models import Category, Blog, Comment

@admin.register(Category)
class BlogCategory(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ['name', 'slug']
    

@admin.register(Blog)
class BlogClass(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    list_display = ['title','slug']
    search_fields = ('title', "created_at")
    list_filter = [ "created_at"]


admin.site.register(Comment)
