from django import forms
# from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import User

import re

class SignUpForm(forms.ModelForm):
    cpassword=forms.CharField(max_length=40,widget=forms.PasswordInput(attrs={'class':'form-control'}),label='Confirm Password')
    # def clean_username(self):
    #     username = self.cleaned_data['username']
    #     if not re.match(r'^[A-Za-z0-9_]+$', username):
    #         raise forms.ValidationError("Enter Valid Username")
    #     return username
    cpassword=forms.CharField(max_length=40,widget=forms.PasswordInput(attrs={'class':'form-control'}),label='Confirm Password')
    def clean_cpassword(self):
            cleaned_data = super().clean()
            p = cleaned_data.get('password')
            cp = cleaned_data.get('cpassword')
            print(p,cp)
            if p != cp:
                raise forms.ValidationError('Password And Confirm Password Do Not Match')
            return cp
    
   
    class Meta:

        model = User
        fields = ['username','first_name','email','password','cpassword']
        widgets = {
        'username':forms.TextInput(attrs={'class':'form-control'}),
        'first_name':forms.TextInput(attrs={'class':'form-control'}),
        'email':forms.EmailInput(attrs={'class':'form-control'}),
        'password':forms.PasswordInput(attrs={'class':'form-control'}),}
        
        error_messages = {

            'username': {
                'required': 'This Field Should not Be Empty',
            },
            'fname': {
                'required': ("This Field Shouldn't Be Empty"),
            },
            'lname': {
                'required': ("This Field Shouldn't Be Empty"),
            },
            'email': {
                'invalid': ("Enter A Valid Email Address"),
            },
            'password': {
                'required': ("This Field Shouldn't Be Empty"),
            },
         
    
        }

        
            





class LoginForm(forms.Form):
    username=forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"form-control"
            }
        )
    )
    
    password=forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control"
            }
            
        )
    )