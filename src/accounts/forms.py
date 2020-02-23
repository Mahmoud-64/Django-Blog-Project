from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from post.models import Post

class SignUpForm(UserCreationForm):
    profile_picture = forms.ImageField()

    class Meta:
        model = User
        fields = ('username', 'profile_picture', 'password1', 'password2', )


class addPostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content','author','cat_id')

