from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.contrib import messages
from post.models import Profile
# Create your views here.
#admin panel page
def admin_panel_page(request):
      return render(request,'admin panel/dashboard.html',{})
      

#all user dashboard
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
def delete_user(request , id):
    user= User.objects.get(id=id)
    user.delete()
    messages.success(request, "The user is deleted")  
    return redirect('/admin/all_users') 
    
   
    
         