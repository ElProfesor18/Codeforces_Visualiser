from django import forms
from .models import UserProfileInfo
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')

class UserProfileInfoForm(forms.ModelForm):
     class Meta():
         model = UserProfileInfo
         fields = ('handle','profile_pic') 

class contactUs(forms.Form):
    name = forms.CharField(label='Name', max_length=200)
    email = forms.CharField(label='Email', max_length=200)

    subject = forms.CharField(label='Subject', max_length=350)
    message = forms.CharField(label='Message', max_length=500)

    copy = forms.BooleanField(label='Send Me a Copied Email')