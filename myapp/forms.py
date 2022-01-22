from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Blog, Comment
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields=['first_name','last_name','email','username','password1','password2']



class BlogForm(ModelForm):
    class  Meta:
        model = Blog
        fields = ['title', 'image', 'description', 'category','tags']
        
class CommetForm(ModelForm):
    class  Meta:
       model = Comment
       fields = ['text']
    
    
class Ozgartirish(UserCreationForm):
    class Mea:
        model = User
        field = ['password','password1',"password2"]