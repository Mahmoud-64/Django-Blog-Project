from django.shortcuts import render,redirect
from post.models import *
from django.http import *
from django.contrib.auth.models import User
from landing_page.forms import *
from landing_page.models import *
from django.contrib.auth.decorators import login_required
from django.db.models import Q
# Create your views here.

def post_page(request,id):
    #post
    post= Post.objects.get(id=id)
    #like
    like_check=len(Like.objects.filter(user_id=request.user,post_id=post))
    #dislike
    dilike_check=len(Dislike.objects.filter(user_id=request.user,post_id=post))
    #data of post
    queryset=Post.objects.select_related('author').get(id=id)
    #data of comments
    comments=Comment.objects.select_related('user_id','post_id').filter(post_id=id)
    #length of comments data
    comments_len=len(comments)
    #create form
    form = CommentForm()
    #check request
    
    if request.method =="POST":
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                #stop save data
                new_comment = form.save(commit=False)
                #fill data
                #get post
                post=Post.objects.get(id=id)
                #pass post data to comment
                new_comment.post_id=post
                new_comment.user_id=request.user
                new_comment.save()
                return redirect('/post/'+id)
            else:
                return render(request,'landing_page/post.html',
                {'queryset':queryset,'form':form,'comments':comments,'comments_len':comments_len
                ,'like_check':like_check ,'dislike_check':dilike_check})

    else:
        #return HttpResponse(queryset.author.username)
        return render(request,'landing_page/post.html',{'queryset':queryset,'form':form,'comments':comments,'comments_len':comments_len
        ,'like_check':like_check ,'dislike_check':dilike_check})

#like
@login_required(login_url='/accounts/login/')
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
#dislike
@login_required(login_url='/accounts/login/')
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


#subscribe
def subscribe(request,u_id,c_id):
    user = User.objects.get(id=u_id)
    cat= Category.objects.get(id=c_id)
    #save data
    data=cat.user_id.add(request.user)
    cat.save(data)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        
def search(request):
    queryset = Post.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(content=query)
        ).distinct()
    return render(request,'landing_page/search_result.html', {'queryset': queryset})                
    
