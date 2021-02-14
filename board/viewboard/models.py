from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class extenduser(models.Model):
    
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    post = models.CharField(max_length=50)
    board = models.CharField(max_length=50)
    instagram = models.CharField(max_length=2200,null=True)
    github = models.CharField(max_length=2048,null=True)
    linkedin = models.CharField(max_length=2000)
    photo = models.ImageField(upload_to='users',null=True, blank=True,default="https://t4.ftcdn.net/jpg/03/46/93/61/360_F_346936114_RaxE6OQogebgAWTalE1myseY1Hbb5qPM.jpg")
    post_pref = models.IntegerField()
    def __str__(self):
        return 'Profile of user: {}'.format(self.user.username)
    @property
    def get_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url
        else:
            return "/users/users/default.jpg"