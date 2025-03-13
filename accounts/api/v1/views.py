from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from .serializer import SignupSerializer, CustomeAuthTokenSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated

from rest_framework.authtoken.models import Token

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

