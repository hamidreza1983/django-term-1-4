from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from .serializer import (
    SignupSerializer,
    CustomeAuthTokenSerializer,
    CustomJwtSerializer,
    ChangePasswordSerializer,
    ResetPasswordSerializer,
    ResetPasswordDoneSerializer,
)
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)
from django.shortcuts import get_object_or_404
from accounts.models import User
from mail_templated import send_mail
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken


class CustomeObtainView(TokenObtainPairView):
    serializer_class = CustomJwtSerializer


class LoginApiView(ObtainAuthToken):
    serializer_class = CustomeAuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key, "email": user.email})


class LogoutApiView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        user.auth_token.delete()
        return Response(
            {"message": "logout successfully"},
            status=status.HTTP_204_NO_CONTENT,
        )


class SignupApiView(GenericAPIView):
    serializer_class = SignupSerializer

    def post(self, request, *args, **kwargs):
        serialize = self.serializer_class(data=request.data)
        serialize.is_valid(raise_exception=True)
        serialize.save()
        email = serialize.validated_data["email"]
        user = User.objects.get(email=email)
        token = self.get_token_for_user(user)
        send_mail(
            "email/verify.html",
            {"user": user, "token": token},
            "admin@my-site.com",
            [user.email],
        )
        return Response(
            {
                "message": "email verification send for you.please check your inbox"
            },
            status=status.HTTP_201_CREATED,
        )

    def get_token_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)


class ChangePassword(GenericAPIView):
    serializer_class = ChangePasswordSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        pk = self.request.user.id
        user = get_object_or_404(User, pk=pk)
        return user

    def put(self, request, *args, **kwargs):
        serialize = ChangePasswordSerializer(
            data=request.data, context={"request": request}
        )
        serialize.is_valid(raise_exception=True)
        serialize.change(serialize.validated_data)
        return Response(
            {"message": "password change successfully"},
            status=status.HTTP_202_ACCEPTED,
        )


class ResetPassword(GenericAPIView):
    serializer_class = ResetPasswordSerializer

    def post(self, request, *args, **kwargs):
        serializer = ResetPasswordSerializer(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = User.objects.get(email=serializer.validated_data["email"])
        token = self.get_token_for_user(user)
        send_mail(
            "email/email.html",
            {"user": user, "token": token},
            "admin@my-site.com",
            [user.email],
        )
        return Response(
            {"message": "email send successfully"},
            status=status.HTTP_202_ACCEPTED,
        )

    def get_token_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)


class ResetPasswordDone(GenericAPIView):
    serializer_class = ResetPasswordDoneSerializer

    def post(self, request, *arg, **kwargs):
        serialize = ResetPasswordDoneSerializer(
            data=request.data, context={"request": request}
        )
        serialize.is_valid(raise_exception=True)
        user_token_obj = AccessToken(kwargs["token"])
        user_id = user_token_obj["user_id"]
        user = get_object_or_404(User, pk=user_id)
        serialize.set_pass(serialize.validated_data, user)
        return Response(
            {"message": "password reset successfully"},
            status=status.HTTP_202_ACCEPTED,
        )


class VerifyDone(APIView):

    def get(self, request, *args, **kwargs):
        token = kwargs.get("token")
        user_token_obj = AccessToken(token)
        user_id = user_token_obj["user_id"]
        user = get_object_or_404(User, pk=user_id)
        user.is_verified = True
        user.save()
        return Response(
            {"message": "your email verified successfully"},
            status=status.HTTP_200_OK,
        )
