from django.shortcuts import render, redirect
from .forms import LoginForm, SignUpForm, ChangePassForm, ResetPassForm, ConfirmPassForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth import password_validation
from rest_framework.authtoken.models import Token
from django.core.mail import send_mail



from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("root:home")
            else:
                messages.add_message(request, messages.ERROR, "Invalid credintial")
                return redirect(request.path_info)

            #username = request.POST.get('username').strip()
    else:
        return render(request, "registration/login.html")


@login_required
def logout_user(request):
    logout(request)
    return redirect("root:home")

def signup_user(request):
     if request.method == 'POST':
         form = SignUpForm(request.POST)
         if form.is_valid():
             user = form.save()
             login(request, user)
             return redirect("root:home")
         else:
                messages.add_message(request, messages.ERROR, "Invalid input data")
                return redirect(request.path_info)
     else:
        return render(request, "registration/signup.html")

@login_required
def change_password(request):
    user = request.user
    if request.method == 'POST':
        form = ChangePassForm(request.POST)
        if form.is_valid():
            pass1 = form.cleaned_data['password1']
            pass2 = form.cleaned_data['password2']
            if (pass1 == pass2) and not (user.check_password(pass1)) :
                try:
                    password_validation.validate_password(pass1)
                except:
                    messages.add_message(request, messages.ERROR, "Invalid password validation")
                    return redirect(request.path_info)
                else:
                    user.set_password(pass1)
                    user.save()
                    login(request, user)
                    messages.add_message(request, messages.SUCCESS, "password change successfully")
                    return redirect(request.path_info)
            else:
                messages.add_message(request, messages.ERROR, "password and pass2 must be similar or different between old and new")
                return redirect(request.path_info)
        else:
            messages.add_message(request, messages.ERROR, "invalid input data")
            return redirect(request.path_info)

    else:
        return render (request, "registration/change-password.html")

def reset_password(request):
    if request.method == "POST":
        form = ResetPassForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                user = User.objects.get(email=email)
            except :
                messages.add_message(request, messages.ERROR, "user not found")
                return redirect(request.path_info)
            else:
                token, create = Token.objects.get_or_create(user=user)
                if not create:
                    Token.objects.get(user=user).delete()
                    token = Token.objects.create(user=user)
                send_mail(
                    "Reset your password",
                    f"""
                    please click on link for  reset password\n
                    http://127.0.0.1:8000/accounts/reset-password-confirm/{token.key}""",
                    "admin@mysite.com",
                    [user.email],
                    fail_silently=True,
                )
                return redirect("accounts:reset_password_done")
        else:
            messages.add_message(request, messages.ERROR, "invalid input data")
            return redirect(request.path_info)          
    else:
        return render (request, "registration/reset-password.html")

def reset_password_done(request):
    return render (request, "registration/reset-password-done.html")

def reset_password_confirm(request, token):
    if request.method == "POST":
        form = ConfirmPassForm(request.POST)
        user = Token.objects.get(key=token).user
        if form.is_valid():
            pass1 = form.cleaned_data['pass1']
            pass2 = form.cleaned_data['pass2']
            if (pass1 == pass2) and not (user.check_password(pass1)) :
                try:
                    password_validation.validate_password(pass1)
                except:
                    messages.add_message(request, messages.ERROR, "Invalid password validation")
                    return redirect(request.path_info)
                else:
                    user.set_password(pass1)
                    user.save()
                    return redirect("accounts:reset_password_complete")
            else:
                messages.add_message(request, messages.ERROR, "password and pass2 must be similar or different between old and new")
                return redirect(request.path_info)
        else:
            messages.add_message(request, messages.ERROR, "invalid input data")
            return redirect(request.path_info)
    else:
        return render (request, "registration/reset-password-confirm.html")

def reset_password_complete(request):
    return render (request, "registration/reset-password-complete.html")

def edit_profile(request):
    pass