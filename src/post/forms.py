from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from post.models import *
from django.forms import ModelForm

class SignUpForm(UserCreationForm):
    profile_picture = forms.ImageField()

    class Meta:
        model = User
        fields = ('username', 'profile_picture','is_active','is_staff','password1', 'password2', )


#post form 
class addPostForm(ModelForm):
    tags=forms.ModelMultipleChoiceField(queryset=Tag.objects.all())
    class Meta:
        model = Post
        fields = ('title', 'content','author','tags','cat_id','post_pic',)

     

    