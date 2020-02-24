from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Tag,Category



class SignUpForm(UserCreationForm):
    profile_picture = forms.ImageField()

    class Meta:
        model = User
        fields = ('username', 'profile_picture','is_active','is_staff','password1', 'password2', )


class TagForm(forms.ModelForm):
	class Meta:
		model= Tag
		fields= ('tag_name',)
	
	
class CategoryForm(forms.ModelForm):
	class Meta:
		model= Category
		fields= ('cat_name',)
	
