from django import forms
from django.forms.fields import CharField, EmailField


class SignupForm(forms.Form):
    name = forms.CharField(label='Name: ', max_length=50)
    email = forms.EmailField(label="Email: ")
    password = forms.CharField(label="Password: ",max_length=50)

class LoginForm(forms.Form):
    email = forms.EmailField(label="Email: ")
    password = forms.CharField(label="Password: ",max_length=50)