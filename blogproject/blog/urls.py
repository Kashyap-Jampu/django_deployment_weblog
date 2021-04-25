from django.urls import path
from . import views

urlpatterns=[
    path('',views.blog,name="blog"),
    path('post/<str:title>/',views.post,name="post"),
    path('comment/',views.postcomment,name="postcomment"),
    path('write_post',views.write_post,name="write_post"),



]
