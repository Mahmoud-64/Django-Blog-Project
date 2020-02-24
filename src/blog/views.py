from django.shortcuts import render
from post.models import *
from django.http import HttpResponse

def index(request):
<<<<<<< HEAD
    queryset = Post.objects.select_related('author')
  
    
    return render(request,'landing_page/index.html',{'objects':queryset})
=======
    queryset = Post.objects.all()
    return render(request,'landing_page/index.html',{'objects':queryset})
    return render(request,'landing_page/index.html',{})
>>>>>>> 99fa75d5e725fe90c32c1d09fc63b044dfc0143d

def blog(request):

    
    return render(request,'landing_page/base.html',{})

def post(request):
    return render(request,'landing_page/post.html',{})



    
