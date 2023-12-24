from django.db import models
from django.contrib.auth.models import User
import uuid
from datetime import datetime
# Create your models here.

class Profile(models.Model):
  user = models.ForeignKey(User,on_delete = models.CASCADE)
  id_user = models.IntegerField(primary_key = True,default=0)
  bio = models.TextField(blank = True,default = '')
  profiling = models.ImageField(upload_to='profile_images',default='blank-profile-picture.png')
  location = models.CharField(max_length = 100,blank = True,default = '')

  def __str__(self):
    return self.user.username
  

class Post(models.Model):
  id = models.UUIDField(primary_key = True,default = uuid.uuid4)
  user = models.CharField(max_length=100)
  image = models.ImageField(upload_to='post_image')
  caption = models.TextField()
  created_at = models.DateTimeField(default= datetime.now)

  def __str__(self):
    return self.user
  
  
  
