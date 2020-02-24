from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

# Create your models here.

User = get_user_model()
#Profile
class Profile(models.Model):
    user = models.OneToOneField(User,related_name='profile', on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='images/')

    def delete(self, *args, **kwargs):
        # You have to prepare what you need before delete the model
        storage, path = self.profile_picture.storage, self.profile_picture.path
        # Delete the model before the file
        super(Profile, self).delete(*args, **kwargs)
        # Delete the file after the model
        storage.delete(path)

#    def __str__(self):
#        return self.user.name   

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()         

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
    author = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
    post_pic = models.ImageField(default='SOME STRING')
    cat_id = models.ForeignKey(Category,on_delete=models.DO_NOTHING)
    featured = models.BooleanField(default=0)

    def get_absolute_url(self):
        return reverse('post_detail',kwargs={
            'id': self.id
        })
        

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
	
