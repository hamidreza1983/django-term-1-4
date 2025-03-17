from rest_framework import serializers
from accounts.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import exceptions
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomJwtSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data["email"] = self.user.email
        return data


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
    

class ChangePasswordSerializer(serializers.Serializer):
    old_pass = serializers.CharField(max_length=20)
    pass1 = serializers.CharField(max_length=20)
    pass2 = serializers.CharField(max_length=20)

    def get_user(self):
        user = self.context.get("request").user
        return user

    def validate(self, attrs):
        old_pass = attrs["old_pass"]
        pass1 = attrs["pass1"]
        pass2 = attrs["pass2"]
        user =self.get_user()
        if not user.check_password(old_pass):
            raise serializers.ValidationError({"details" : "old pass is not correct"})
        if pass1 != pass2 or pass1 == old_pass or pass2 == old_pass:
            raise serializers.ValidationError({"details" : "pass1 and pass2 must be same and don must be same as old pass"})
        try:
            validate_password(pass1)
        except exceptions.ValidationError as e:
            raise serializers.ValidationError(
               {
                    "message" : list(e.messages)
               }
            )
        return attrs
    
    def change(self, validated_data):
        user = self.get_user()
        pass1 = validated_data["pass1"]
        user.set_password(pass1)
        user.save()
        return validated_data


class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()


class ResetPasswordDoneSerializer(serializers.Serializer):
    pass1 = serializers.CharField(max_length=20)
    pass2 = serializers.CharField(max_length=20)

    def validate(self, attrs):
        pass1 = attrs["pass1"]
        pass2 = attrs["pass2"]
        if pass1 != pass2:
            raise serializers.ValidationError({"details" : "pass1 and pass2 must be same and don must be same as old pass"})
        try:
            validate_password(pass1)
        except exceptions.ValidationError as e:
            raise serializers.ValidationError(
               {
                    "message" : list(e.messages)
               }
            )
        return attrs
    
    def set_pass(self, validated_data, user):
        pass1 = validated_data["pass1"]
        user.set_password(pass1)
        user.save()
        return validated_data