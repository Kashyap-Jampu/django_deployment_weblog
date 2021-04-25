from django.urls import path
from . import views

urlpatterns=[

    path('login',views.login_view,name="login_view"),
    path('register',views.register_view,name="register_view"),
    path('',views.logout_view,name="logout_view"),
    path('forgotpass',views.forgotpass,name="forgotpass"),
    path('pro-pic',views.profile_picc,name="profile_picc"),

]
