from django.shortcuts import render
from post.models import Post

def index(request):
<<<<<<< HEAD
    queryset = Post.objects.all()
    return render(request,'landing_page/index.html',{'objects':queryset})
=======
    return render(request,'landing_page/index.html',{})
>>>>>>> d58c80eeb79e4f8b7b31d0dee256a7263f19e46a

def blog(request):

    
    return render(request,'landing_page/base.html',{})

def post(request):
    return render(request,'landing_page/post.html',{})



    
