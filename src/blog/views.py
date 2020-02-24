from django.shortcuts import render
from post.models import Post

def index(request):
    queryset = Post.objects.all()
    return render(request,'landing_page/index.html',{'objects':queryset})

def blog(request):
    return render(request,'landing_page/base.html',{})

def post(request,id):
    return render(request,'landing_page/post.html',{})



    
