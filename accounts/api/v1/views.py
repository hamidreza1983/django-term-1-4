from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from .serializer import (
    SignupSerializer, 
    CustomeAuthTokenSerializer, 
    CustomJwtSerializer,
    ChangePasswordSerializer
)
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)
from django.shortcuts import  get_object_or_404
from accounts.models import User


class CustomeObtainView(TokenObtainPairView):
    serializer_class = CustomJwtSerializer




class LoginApiView(ObtainAuthToken):
    serializer_class = CustomeAuthTokenSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'email':user.email})


class LogoutApiView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        user = request.user
        user.auth_token.delete()
        return Response({'message': "logout successfully"}, status=status.HTTP_204_NO_CONTENT)


class SignupApiView(GenericAPIView):
    serializer_class = SignupSerializer

    def post(self, request, *args, **kwargs):
        serialize = self.serializer_class(data=request.data)
        serialize.is_valid(raise_exception=True)  
        serialize.save()
        return Response({"message" : "user created successfully"}, status=status.HTTP_201_CREATED)
    

class ChangePassword(GenericAPIView):
    serializer_class = ChangePasswordSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        pk = self.request.user.id
        user = get_object_or_404(User, pk=pk)
        return user

    def put(self, request, *args, **kwargs):
        serialize = ChangePasswordSerializer(data=request.data, context={"request" : request})
        serialize.is_valid(raise_exception=True)
        serialize.change(serialize.validated_data)
        return Response({"message" : "password change successfully"}, status=status.HTTP_202_ACCEPTED)
