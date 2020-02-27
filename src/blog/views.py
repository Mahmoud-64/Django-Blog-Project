from django.shortcuts import render
from post.models import *
from django.http import HttpResponse

def index(request):
    queryset = Post.objects.select_related('author')
    
    
    return render(request,'landing_page/index.html',{'objects':queryset})

def blog(request):
    cat=Category.objects.all()[:5]
    tag=Tag.objects.all()
    return render(request,'landing_page/base.html',{'tags':tag,'all':cat})

    
def post(request):
    return render(request,'landing_page/post.html',{})



    
