from django import forms
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)


class SignUpForm(UserCreationForm):
    email = forms.EmailField()


class ChangePassForm(forms.Form):
    password1 = forms.CharField(max_length=15)
    password2 = forms.CharField(max_length=15)


class ResetPassForm(forms.Form):
    email = forms.EmailField()

class ConfirmPassForm(forms.Form):
    pass1 = forms.CharField(max_length=15)
    pass2 = forms.CharField(max_length=15)