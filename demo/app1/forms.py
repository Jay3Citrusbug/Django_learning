from django import forms
# from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth.models import User

import re

class SignUpForm(forms.ModelForm):
    cpassword=forms.CharField(max_length=40,widget=forms.PasswordInput(attrs={'class':'form-control'}),label='Confirm Password')
    # def clean_username(self):
    #     username = self.cleaned_data['username']
    #     if not re.match(r'^[A-Za-z0-9_]+$', username):
    #         raise forms.ValidationError("Enter Valid Username")
    #     return username
    
    def clean_cpassword(self):
            cleaned_data = super().clean()
            p = cleaned_data.get('password')
            cp = cleaned_data.get('cpassword')
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
        
    
    def save(self, commit=True):
        instance = super(SignUpForm, self).save(commit=False)
        instance.password = self.cleaned_data["password"]
        instance.password=make_password(instance.password)
        if commit:
            instance.save()
        return instance

    
            





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
    
    
class ChangepassForm(forms.Form):
 
        
        password1=forms.CharField(
            widget=forms.PasswordInput(
                attrs={
                    "class":"form-control"
                }
                
            )
        )
        
        password2=forms.CharField(
            widget=forms.PasswordInput(
                attrs={
                    "class":"form-control"
                }
                
            )
        )




# class forgetpass(forms.Form):
#     email = forms.EmailField(max_length=60)


# class forgetpass1(forms.Form):
    
#     password =  forms.CharField(widget=forms.PasswordInput())
#     confirmpassword= forms.CharField(widget=forms.PasswordInput())


class forgetpass(forms.Form):
   
    email = forms.EmailField()

class Reset(forms.Form):
    new_password = forms.CharField(widget=forms.PasswordInput())
    reenter_password = forms.CharField(widget=forms.PasswordInput())
    
    def clean(self):
        
        cleaned_data = super().clean()
        
        np = cleaned_data.get('new_password')
        rep = cleaned_data.get('reenter_password')


        if np is None:
            self.add_error("new_password", "enter valid new password")
        if rep is None:
            self.add_error("reenter_password", "type reenter password")
        if np is  not None and rep is not None and rep is not None:
            if len(np) < 8:
                self.add_error('new_password','new_password is too short')
        
            
            if rep!=np:
                self.add_error("reenter_password","mismatch")
        return cleaned_data