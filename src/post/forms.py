from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Comment

class SignUpForm(UserCreationForm):
    profile_picture = forms.ImageField()

    class Meta:
        model = User
        fields = ('username', 'profile_picture','is_active','is_staff','password1', 'password2', )


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Type your comment',
        'id': 'usercomment',
        'rows': '4'
    }))
    class Meta:
        model = Comment
        fields = ('content', )