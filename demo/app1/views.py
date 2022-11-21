from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.views import LoginView,PasswordChangeView,PasswordChangeDoneView,PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.hashers import make_password,check_password
from .forms import SignUpForm,LoginForm,forgetpass,Reset
from django import forms
from django.core.mail import send_mail
# Create your views here.
import re
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
     return render(request,'home.html')




class changepass(PasswordChangeView):
    template_name='changepass.html'
   #  success_url='/logout'
   
class changepassdone(PasswordChangeDoneView):
    template_name='password_change_done.html'
   #  success_url='/logout
   
  
   
   

   
   
   
   
# class PasswordResetView(PasswordResetView):
#     template_name='password_reset.html'
#    #  success_url = '/app1/password_reset_confirm'

# class PasswordResetDoneView(PasswordResetDoneView):
#     template_name='password_reset_done.html'
    
# class PasswordResetConfirmView(PasswordResetConfirmView):
#     template_name='password_reset_confirm.html'



# class PasswordResetCompleteView(PasswordResetCompleteView):
#     template_name='password_reset_complete.html'
   
# def forget(request):
#       form = forgetpass(request.POST)
#       if request.method  == 'POST':
#         if form.is_valid():
#             email =  form.cleaned_data.get('email')
#             password =  form.cleaned_data.get('password')
#             password1 =  form.cleaned_data.get('confirmpassword')
#             print("********************",form.cleaned_data.get('email'))
#             print(email,password,password1)
#             if User.objects.filter(email=email).exists():
#                 if password==password1:
#                     if len(password)<8:
#                         return HttpResponse("password greater then 8 characeters")
#                     else:
#                         user=User.objects.get(email=email)
#                         user.set_password(password)
#                         user.save()
#                         return redirect('login')
#             return HttpResponse("password and confirm password are not match")
#       return render(request,'forget.html',{'form':form})

def forgetpassword(request):
   
    if request.method == 'POST':
        
        form = forgetpass(request.POST)
        if form.is_valid():
          email  = form.cleaned_data.get('email') 
          if User.objects.filter(email=email).exists():
            recent_user = User.objects.get(email = email)
            id = recent_user.id
            context = {
                "user":recent_user,
            }
            return redirect("Resset", pk = id)
           
          else:
            return HttpResponse("NO User exist, please register first")
        else:
            form  = forgetpass(request.POST)
            return render(request, "forget.html") 
    else:
        form  = forgetpass()
        return render(request,"forget.html",{'form':form})
    
    
def reset(request,pk):
    
   
    if request.method == 'POST':

        form = Reset(request.POST)
        if form.is_valid():
            new_password = form.cleaned_data.get('new_password')
            user  = User.objects.get(id = pk)
            user.set_password(new_password)
            user.save()

            return HttpResponse("password has been reset")
        else:

            form = Reset(request.POST)
            return render(request, "reset.html",{'form':form})  
    else:
        form = Reset()
        return render(request,"reset.html",{'form':form})
