from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import AbstractUser
# from .manager import Usermanager

# Create your models here.


class User(AbstractBaseUser):
    username=None
    email=models.EmailField(unique=True)
    mobile=models.CharField(max_length=14) 
    
    email_token=models.CharField(max_length=100,null=True,blank=True)    
    is_verified=models.BooleanField(default=False)
    forgot_password=models.CharField(max_length=100,null=True,blank=True)
    last_login_time=models.DateTimeField(null=True,blank=True)
    last_logout_time=models.DateTimeField(null=True,blank=True)
    
  
    
    USERNAME_FIELD = 'email'
    
    REQUIRED_FIELDS= []