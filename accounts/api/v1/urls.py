from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)

app_name = "api-accounts"

urlpatterns = [
    path("login/",LoginApiView.as_view(), name="login"),
    #path("login/",ObtainAuthToken.as_view(), name="login"),
    path("logout/",LogoutApiView.as_view(), name="logout"),
    path("signup/",SignupApiView.as_view(), name="signup"),
    path('jwt/login/', CustomeObtainView.as_view(), name='token_obtain_pair'),
    path('jwt/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('jwt/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('change-password/', ChangePassword.as_view(), name='token_verify'),
]