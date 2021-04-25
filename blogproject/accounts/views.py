from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import profile_pic

# Create your views here.
def profile_picc(request):
    if request.method=='POST':
        u_id=request.POST['u_id']
        u=User.objects.get(id=u_id)
        profile_img= request.FILES.get('profile_img')
        p_pic=profile_pic(user=u,profile_pics=profile_img)
        p_pic.save()
        print(u_id)
        return redirect('/')

    return render(request,'users/profie_pic.html')
def register_view(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']

        if User.objects.filter(username=email).exists():
            messages.info(request,'EMAIL ALREADY IN USE ')
            return render(request,'users/signup.html')

        else:
            users=User.objects.create_user(username=email,first_name=name ,password=password,email=email)
            users.save()
        return redirect('login_view')
    return render(request,'users/signup.html')

def login_view(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        users = authenticate(request, username=email, password=password)
        if users is not None:
            login(request, users)
            return redirect('/')
        else:
            messages.info(request,'ERROR IN LOGIN!!!')


    return render(request,'users/login.html')

def logout_view(request):
    logout(request)
    return redirect('/')

def forgotpass(request):
    if request.method=='POST':
        email=request.POST['email']
        newpassword=request.POST['password']
        u = User.objects.get(username=email)
        u.set_password(newpassword)
        u.save()
        messages.info(request,'reset done ')
        return redirect('login_view')

    return render(request,'users/forgot_password.html')
