from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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