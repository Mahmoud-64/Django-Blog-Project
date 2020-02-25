from django.shortcuts import render
from post.models import Post
from post.forms import CommentForm

def index(request):

    queryset = Post.objects.all()
    return render(request,'landing_page/index.html',{'objects':queryset})

def blog(request):
    return render(request,'landing_page/base.html',{})

def post(request,id):
    queryset=Post.objects.get(id = id)
    form = CommentForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            post = self.get_object()
            form.instance.user = request.user
            form.instance.post = post
            form.save()
            return redirect(reverse("post-detail", kwargs={
                'pk': post.pk
            }))
    return render(request,'landing_page/post.html',{'queryset':queryset,'form':form})
