from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.contrib import messages
from post.models import *
from post.forms import *
from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.
#admin panel page
@staff_member_required(login_url="/account/login")
def admin_panel_page(request):
      return render(request,'admin panel/dashboard.html',{})
      

#all user dashboard
@staff_member_required(login_url="/account/login")
def all_users(request):
    user_list = User.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(user_list, 5)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return render(request ,'admin panel/users/all_users.html',{ 'users': users })



#delete user
@staff_member_required(login_url="/account/login")
def delete_user(request , id):
    user= User.objects.get(id=id)
    user.delete() 
    messages.error(request, "The user is deleted") 
    return redirect('/admin/all_users') 
    


#edit user
@staff_member_required(login_url="/account/login")
def edit_user(request,id):
    user= User.objects.get(id=id)
    if request.method == 'POST':
        form= SignUpForm(request.POST, request.FILES,instance=user)
        if form.is_valid():
            user=form.save()
            user.refresh_from_db()
            user.profile.profile_picture = form.cleaned_data.get('profile_picture')
            user.save()
            messages.success(request, "The user Edited") 
            return redirect('/admin/all_users') 
    else:
        form= SignUpForm(instance=user)
        return render(request,'admin panel/users/edit_user.html',{'user': user,'form':form})

#add user
@staff_member_required(login_url="/account/login")
def add_user(request): 
    if request.method == 'POST':
        form= SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user=form.save()
            user.refresh_from_db()
            user.profile.profile_picture = form.cleaned_data.get('profile_picture')
            user.save()
            messages.success(request, "The user Edited") 
            return redirect('/admin/all_users') 
    else:
        form= SignUpForm()
        return render(request,'admin panel/users/add_user.html',{'form':form})   

#blog section
#add blog
@staff_member_required(login_url="/account/login")
def add_post_view(request):
    
    if request.method =="POST":
        form = addPostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            #data.tags=1
            #data.save()
            return redirect("/admin/admin_posts_table/")
    else:
        form = addPostForm()        
        return render(request, 'admin panel/posts/addPostForm.html', {'form':form})

#all blog
@staff_member_required(login_url="/account/login")
def view_all_posts(request):
    queryset = Post.objects.all()
    return render(request,'admin panel/posts/all_posts.html',{'objects':queryset})
@staff_member_required(login_url="account/login")
def delete_posts(request,id):
    obj = Post.objects.get(id=id)
    obj.delete()
    return redirect('http://localhost:8000/account/admin_posts_table/') 

#edit post
@staff_member_required(login_url="/account/login")
def edit_post(request,id):
    post = Post.objects.get(id=id)
    if request.method =="POST":
        form = addPostForm(request.POST,instance=post)
        if form.is_valid():
            post.save()
            return redirect("/admin/admin_posts_table/")
    else:
        form = addPostForm(instance=post)
        return render(request, 'admin panel/posts/editPostForm.html', {'form':form})
    
         