from django.urls import path
from .views import *


app_name = "accounts"

urlpatterns = [
    path("login/",LoginView.as_view(), name="login"),
    path("logout/",logout_user, name="logout"),
    path("signup/",signup_user, name="signup"),
    path("change-password/",change_password, name="change_password"),
    path("reset-password/",reset_password, name="reset_password"),
    path("reset-password-done/",reset_password_done, name="reset_password_done"),
    path("reset-password-confirm/<str:token>",reset_password_confirm, name="reset_password_confirm"),
    path("reset-password-complete/", reset_password_complete, name="reset_password_complete"),
    path("edit-profile/<int:id>",edit_profile, name="edit_profile"),
]
