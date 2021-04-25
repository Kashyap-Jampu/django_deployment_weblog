from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class profile_pic(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='profile_pic_users')
    profile_pics=models.ImageField(upload_to='users/profile_pics',blank=True,null=True)

    def __str__(self):
        return self.user.email
