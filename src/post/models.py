from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()
#author
class Author(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	profile_picture=models.ImageField(default='SOME STRING')
	def __str__(self):
		return self.user.username
#post
class Post(models.Model):
	title = models.CharField(max_length=100);
	content= models.TextField()
	timestamp= models.DateTimeField(auto_now_add=True)
	comment_count=models.IntegerField(default=0)
	author=models.ForeignKey(Author,on_delete=models.CASCADE)
	post_pic = models.ImageField(default='SOME STRING')
	cat_id=models.ForeignKey(Category)
	featured=models.BooleanField(default=0)
	def __str__(self):
		return self.title


#tags
class Tag(models.Model):
	tag_name= models.CharField(max_length=150)
	
	


	def __str__(self):
		return self.tag_name
#category
class Category(models.Model):
	category_name= models.CharField(max_length=150)
	def __str__(self):
		return self.category_name
#comments
class Comment(models.Model):
    comment_content=models.TextField()
    user_id=models.ForeignKey(User)
    post_id=models.ForeignKey(Post)
    timestamp= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_content


