from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.contrib import messages
from post.models import Profile ,Tag ,Category
from post.forms import SignUpForm ,TagForm, CategoryForm
from django.http import HttpResponseRedirect

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
    messages.error(request, "The user is deleted") 
    return redirect('/admin/all_users') 
    


#edit user
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


#category section
#view all categories
def category(request):
	all=Category.objects.all()
	context={'all':all}
	return render(request,'admin panel/categories/category.html',context)

#add cat
def add_cat(request):
	form = CategoryForm()
	if request.method=="POST":
		form= CategoryForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/categories')

	return render(request , 'admin panel/categories/edit.html',{'form':form})

#edit category
def edit_cat(request, id):
	ct = "<h1> edit category that have id : ",id,"</h1>"
	cat=Category.objects.get(id=id)
	
	if request.method=="POST":
		form= CategoryForm(request.POST,instance=cat)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/categories')
	else:
		form= CategoryForm(instance=cat)

	return render (request, 'admin panel/categories/edit.html',{'form':form})

#delete category

def del_cat(request, id):
	ct = "<h1> delete category that have id : ",id,"</h1>"
	cat=Category.objects.get(id=id)
	cat.delete()
	return HttpResponseRedirect('/categories')


#tag section
#add tag
def add_tag(request):
	form = TagForm()
	if request.method=="POST":
		form= TagForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/tags')
	return render(request , 'admin panel/tags/edit.html',{'form':form})

#view all tags
def tags(request):
	all=Tag.objects.all()
	context={'all':all}
	return render(request,'admin panel/tags/tags.html',context)

#edit tag
def edit_tag(request, id):
	tg = "<h1> edit Tag that have id : ",id,"</h1>"
	tag=Tag.objects.get(id=id)
	
	if request.method=="POST":
		form= TagForm(request.POST,instance=tag)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/tags')
	else:
		form= TagForm(instance=tag)

	return render (request, 'admin panel/tags/edit.html',{'form':form})

#delete tag

def del_tag(request, id):
	st = "<h1> delete tag that have id : ",id,"</h1>"
	std=Tag.objects.get(id=id)
	std.delete()
	return HttpResponseRedirect('/tags')



    
         