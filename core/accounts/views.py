from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login
# Create your views here.

def register(request):
    if request.method=="POST":
        full_name=request.POST.get('full_name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=User.objects.filter(username=full_name)
        if user.exists():
            messages.error(request,'Username already exist')
            return redirect('register')
        user=User.objects.create(
            username=full_name,
            email=email,
            )
        user.set_password(password)
        user.save()
        return redirect('login_page')
    return render(request,"register.html")

def login_page(request):
    if request.method=="POST":
        full_name=request.POST.get('full_name')
        password=request.POST.get('password')
        if not User.objects.filter(username=full_name).exists():
            messages.error(request,'Invalid User')
            return redirect('login_page')
        
        user=authenticate(username=full_name,password=password)
        if user is None:
            messages.error(request,'InvalidPassword')
            return redirect('login_page')
        
        login(request,user)
        return redirect('/quizoSphere/get_quiz')
        
    return render(request,"login.html")
