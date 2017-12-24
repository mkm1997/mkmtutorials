from .models import usersignup,contact
from django import forms
from django.contrib.auth.models import User



class signup(forms.ModelForm):

    password = forms.CharField(widget= forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

class info(forms.ModelForm):
    class Meta():
        model = contact
        fields = ('name','email','contactno','query')