from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login
from accounts.forms import SignUpForm
from post.models import Post
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth import logout

# Create your views here.
from django.shortcuts import render
#UserCreationForm
def signup_view(request):
    if request.method == 'POST':
        form= SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user=form.save()
            user.refresh_from_db()
            user.profile.profile_picture = form.cleaned_data.get('profile_picture')
            user.save()
            login(request,user)
            return redirect("/blog")
    else:
        form= SignUpForm()
    return render(request,'auth/sign up.html',{'form':form})

#login 
def login_view(request):
    if request.method == 'POST':
        form= AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            
            return redirect("/blog")
    else:
        form= AuthenticationForm()
    return render(request,'auth/login.html',{'form':form})

#logout
def logout_view(request):
    logout(request)    
    return redirect("/account/login")  



