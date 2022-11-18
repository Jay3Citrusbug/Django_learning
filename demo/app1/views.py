from django.shortcuts import render,redirect
from django.http import HttpResponse
# from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.hashers import make_password,check_password
from .forms import SignUpForm,LoginForm #ChangepassForm
from django import forms
# Create your views here.

def sign_up(request):
  
     msg = None
     if request.method == 'POST':
        form = SignUpForm(request.POST)
      #   print("##################",form)
      #   print(form)
         
      
        if form.is_valid():
            # password = form.cleaned_data.get('password')
            # password=make_password(password)
            # print('##################',password)
            form.save()
            return redirect('login')
        else:
            msg = 'form is not valid'
     else:
        form = SignUpForm()
     return render(request,'signup.html', {'form': form, 'msg': msg})
 
 

def sign_in(request):
    msg=None
    form = LoginForm(request.POST)
   #  print(form) 
    if request.method == 'POST':
         if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            # print(username,password)
            # get_user = User.objects.filter(username=username).first()
            # print(get_user, "get_user")
            # if get_user.check_password(password):
            #    print("true")
            user = auth.authenticate(username=username, password=password)
            print(user)
            if user is not None:
               auth.login(request, user)
               return redirect("home")
            else:
               return HttpResponse("<h1>please enter valid data</h1>")
               
         else:
            msg = 'error validating form'
           
    return render(request, 'login.html', {'form': form, 'msg': msg})

   
    
def home(request):
     return HttpResponse("<h1>welcome</h1>")



# def changepass(request):
#    if request.method == 'POST':
#       form = ChangepassForm(request.POST)
#       if form.is_valid():
#           form.save()
#    else:
#       form = SignUpForm()
#    return render(request,'changepass.html', {'form': form})
          
         
      