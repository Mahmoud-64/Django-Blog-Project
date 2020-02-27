from django.shortcuts import render,redirect
from post.models import *
from django.http import *
from django.contrib.auth.models import User
from landing_page.forms import *
from landing_page.models import *
from django.shortcuts import get_object_or_404
from django.db.models import Q
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

def dislike(request,u_id,p_id):
    #user
    user=User.objects.get(id=u_id)
    #post
    post=Post.objects.get(id=p_id)  
    #check_user_dislike
    user_dislike=Dislike.objects.filter(post_id=post,user_id=user)
    if(len(user_dislike)!=0):
        user_dislike.delete()
    else:    
        #Dislike
        dislike=Dislike(user_id=user,post_id=post)
        #save Dislike in DB
        dislike.save()
    #check for remove post
    #check_dislike_post
    check_dislike= Dislike.objects.filter(post_id=post)
    #check
    if(len(check_dislike)<9):
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        post.delete()  
        return redirect('/')
        
                
    
def search(request):
    queryset = Post.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(content=query)
        ).distinct()
    return render(request,'landing_page/search_result.html', {'queryset': queryset})
