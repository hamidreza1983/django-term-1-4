from rest_framework import serializers
from accounts.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import exceptions


class SignupSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["email", "password"]

    def validate(self, attrs):
        password = attrs["password"]
        try:
            validate_password(password)
        except exceptions.ValidationError as e:
            raise serializers.ValidationError(
               {
                    "message" : list(e.messages)
               }
            )
        return super().validate(attrs)
    

    def create(self, validated_data):
        email = validated_data["email"]
        password = validated_data["password"]
        user = User.objects.create_user(email, password)
        return user
    

from django.utils.translation import gettext_lazy as _
from django.contrib.auth import authenticate

class CustomeAuthTokenSerializer(serializers.Serializer):
    email = serializers.CharField(
        label=_("Email"),
        write_only=True
    )
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )
    token = serializers.CharField(
        label=_("Token"),
        read_only=True
    )

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'),
                                username=email, password=password)

            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs