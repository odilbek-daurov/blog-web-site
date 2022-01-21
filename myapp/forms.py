from django.forms import ModelForm

from .models import Blog, Comment

class BlogForm(ModelForm):
    class  Meta:
        model = Blog
        fields = ['title', 'image', 'description', 'category','tags']
        
class CommetForm(ModelForm):
    class  Meta:
       model = Comment
       fields = ['text']
       