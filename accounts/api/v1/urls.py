from django.urls import path
from .views import *



app_name = "api-accounts"

urlpatterns = [
    path("login/",LoginApiView.as_view(), name="login"),
    #path("login/",ObtainAuthToken.as_view(), name="login"),
    path("logout/",LogoutApiView.as_view(), name="logout"),
    path("signup/",SignupApiView.as_view(), name="signup"),
]