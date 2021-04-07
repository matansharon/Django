from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login,logout
# Create your views here.
def signup(request):
    if request.method =="GET":
        return render(request,'signup.html',{"form":UserCreationForm()})
    else:
        if request.POST["password1"]== request.POST["password2"]:
            try:
                user= User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('current')
                # return render(request,'home.html',{"form":UserCreationForm()})
            except IntegrityError:
                return render(request,'signup.html',{'form':UserCreationForm(),'error':"user name already taken"})
        else:
            return render(request,'signup.html',{'form':UserCreationForm(),'error':"password dont match"})
def current(request):
    return render(request,'current.html')

def home(request):
    return render(request,'home.html')

def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return render(request,'home.html')
def login_user(request):
    pass