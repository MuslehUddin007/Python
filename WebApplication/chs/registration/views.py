from django.shortcuts import render
from . models import UserInfo
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse

def home(request):
    return render(request,'home.html')


def signup(request):
    return render(request,'signup.html')

def user_login(request):
    return render(request,'login.html')

def send(request):
    fullname = request.POST.get("fn")
    phone = request.POST.get("ph")
    email = request.POST.get("em")
    password = request.POST.get("pa")
    p = UserInfo(user_name = fullname,user_phone = phone,user_email = email,user_password = password)
    p.save()
    return render(request,'login.html',{'message':'Registered! Now Log In'})

def success(request):
    return render(request,'success.html')

def check(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username = email, password = password)
        if user: 
            login(request,user)
            return render(request,'success.html')
        else:
            content = {'error':'Provide valid credentials !!'}
            return render(request,'login.html',content)
    else:
        return render(request,'login.html')
