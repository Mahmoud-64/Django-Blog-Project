from django.shortcuts import render,redirect
from post.models import *
from django.http import HttpResponse
from landing_page.forms import *
# Create your views here.
def post_page(request,id):
    queryset=Post.objects.select_related('author').get(id=id)
    form = CommentForm()
    if request.method =="POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post/'+id)
    else:
        #return HttpResponse(queryset.author.username)
        return render(request,'landing_page/post.html',{'queryset':queryset,'form':form})