from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class category(models.Model):
    name=models.CharField(max_length=255,default='unknown')
    create=models.DateTimeField(default=datetime.now)



    class Meta:
        verbose_name='category'
        verbose_name_plural='categories'
    def __str__(self):
        return self.name


class Post(models.Model):
    categoryy=models.ForeignKey(category,on_delete=models.CASCADE,related_name='categories')
    title=models.CharField(max_length=255)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='users')
    thumbnail=models.ImageField(upload_to='post/thumbnail')
    discreption=models.TextField()
    tags=models.CharField(max_length=255)
    posted_at=models.DateField(default=datetime.now)
    is_published=models.BooleanField(default=False)






    class Meta:
        verbose_name='Post'
        verbose_name_plural='Posts'
    def __str__(self):
        return self.title

class comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='posts_com')

    namee=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    comment=models.TextField()
    commented_at=models.DateTimeField(default=datetime.now)
    is_resolved=models.BooleanField(default=False)



    class Meta:
        verbose_name='comment'
        verbose_name_plural='comments'
    def __str__(self):
        return self.namee
