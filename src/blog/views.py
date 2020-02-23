from django.shortcuts import render

def index(request):
    return render(request,'index.html',{})

def blog(request):
    return render(request,'landing_page/base.html',{})

def post(request):
    return render(request,'landing_page/post.html',{})



    
