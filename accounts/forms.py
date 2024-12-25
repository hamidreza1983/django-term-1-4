from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from captcha.fields import CaptchaField

class Captcha(forms.Form):
    captcha = CaptchaField()

    
class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    captcha = CaptchaField()


class SignUpForm(UserCreationForm):
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ["username", "password1", "password2", "id_code", "phone", "email"]


class ChangePassForm(forms.Form):
    password1 = forms.CharField(max_length=15)
    password2 = forms.CharField(max_length=15)


class ResetPassForm(forms.Form):
    email = forms.EmailField()

class ConfirmPassForm(forms.Form):
    pass1 = forms.CharField(max_length=15)
    pass2 = forms.CharField(max_length=15)

class EditProfile(forms.ModelForm):

    class Meta:
        model = User
        fields = ["id_code", "phone", "image"]