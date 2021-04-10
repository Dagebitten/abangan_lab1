from django.db import models

class User(models.Model):
    user_name = models.CharField(max_length=100)
    user_profilePicture =  models.ImageField(default='default.jpg',upload_to='profile_pics')
    user_profileBio = models.CharField(max_length=500)
    user_keys = models.CharField(max_length=100)
    user_weekTasks  = models.CharField(max_length=200)
    user_todayTasks = models.CharField(max_length=200)

# Create your models here.
