from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()
#author


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(default='SOME STRING')

    def __str__(self):
        return self.user.name

#category
class Category(models.Model):
    cat_name = models.TextField(max_length=150,default='No Cat',editable=True)

    def __str__(self):
        return self.cat_name
#post
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    comment_count = models.IntegerField(default=0)
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)
    post_pic = models.ImageField(default='SOME STRING')
    cat_id = models.ForeignKey(Category,on_delete=models.DO_NOTHING)
    featured = models.BooleanField(default=0)

    def __str__(self):
        return self.title
#tags
class Tag(models.Model):
    tag_name = models.CharField(max_length=150)

    def __str__(self):
        return self.tag_name

#comments
class Comment(models.Model):
    comment_content = models.TextField()
    user_id = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    post_id = models.ForeignKey(Post,on_delete=models.DO_NOTHING)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_content

#tag_post
class Tag_post(models.Model):
	post_id=models.ForeignKey(Post,on_delete=models.DO_NOTHING)
	tag_id=models.ForeignKey(Tag,on_delete=models.DO_NOTHING)
	def __str__(self):
		return self.post_id
	

#Cat_User
class Cat_user(models.Model):
	user_id=models.ForeignKey(User,on_delete=models.DO_NOTHING)
	cat_id=models.ForeignKey(Category,on_delete=models.DO_NOTHING)
	def __str__(self):
		return self.user_id
	