from django.shortcuts import render,redirect
from post.models import *
from django.http import *
from django.contrib.auth.models import User
from landing_page.forms import *
from landing_page.models import *
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

#like
def like(request,u_id,p_id):
    #user 
    user = User.objects.get(id=u_id)
    #post
    post= Post.objects.get(id=p_id)
    #save data
    check_like=Like.objects.filter(user_id=user,post_id=post)
    if(len(check_like)!=0):
        check_like.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else: 
        like=Like(user_id=user,post_id=post)
        like.save()  
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
