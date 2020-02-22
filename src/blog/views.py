from django.shortcuts import render

def index(request):
    return render(request,'landing_page/index.html',{})

def blog(request):
<<<<<<< HEAD
    return render(request,'landing_page/body.html',{})
=======
    return render(request,'landing_page/base.html',{})
>>>>>>> d1f6ca8a5ec5a0d846d524447a79f58d98355f22

def post(request):
    return render(request,'landing_page/post.html',{})



    
