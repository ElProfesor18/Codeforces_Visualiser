from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfileInfo(models.Model):
  user = models.OneToOneField(User,on_delete=models.CASCADE)
  handle = models.CharField(max_length=35)
  profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

  def __str__(self):
    return self.user.username 

class enquiry(models.Model):
  name = models.CharField(max_length = 200)
  email = models.CharField(max_length = 200)

  subject = models.CharField(max_length = 350)
  message = models.CharField(max_length = 500)

  copy = models.BooleanField(default=False)

  def __str__(self):
    return self.name