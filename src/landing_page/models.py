from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from post.models import Post
# Create your models here.
#user
User = get_user_model()
#like 
class Like(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    post_id=models.ForeignKey(Post,on_delete=models.CASCADE)   
#dislike
class Dislike(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    post_id=models.ForeignKey(Post,on_delete=models.CASCADE)    