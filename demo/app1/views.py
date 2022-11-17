from django.shortcuts import render,redirect
from django.http import HttpResponse
# from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.contrib import auth

from .forms import SignUpForm,LoginForm
from django import forms
# Create your views here.

def sign_up(request):
  
     msg = None
     if request.method == 'POST':
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            form.save()
            msg = 'user created'
            return redirect('login')
        else:
            msg = 'form is not valid'
     else:
        form = SignUpForm()
     return render(request,'signup.html', {'form': form, 'msg': msg})
 
 

def sign_in(request):
    msg=None
    form = LoginForm(request.POST)
    print(form) 
    if request.method == 'POST':
         if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = auth.authenticate(username=username, password=password)
            print(user)
            if user is not None:
               auth.login(request, user)
               return redirect("home")
            else:
               print("**********************")
               return HttpResponse("<h1>welcome</h1>")
         else:
            msg = 'error validating form'
           
    return render(request, 'login.html', {'form': form, 'msg': msg})

   
    
def home(request):
     return HttpResponse("<h1>welcome</h1>",request.user)



