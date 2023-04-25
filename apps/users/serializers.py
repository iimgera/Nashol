from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from djoser.serializers import (
    UserCreateSerializer,
    UserSerializer
)

from apps.users.models import User


User = get_user_model()


class UserTokenSerializer(serializers.ModelSerializer):
    access_token = serializers.CharField()
    refresh_token = serializers.CharField()

    class Meta:
        fields = (
            'access_token',
            'refresh_token',
        )


class RegistrationSerializer(UserCreateSerializer):
    password = serializers.CharField(
        write_only=True
    )

    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = (
            'id',
            'email',
            'username',
            'password',
        )


class AuthSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise serializers.ValidationError('User does not exist.')

        if not user.check_password(password):
            raise serializers.ValidationError('Invalid password.')

        refresh = RefreshToken.for_user(user)

        return {
            'user_id': user.id,
            'refresh_token': str(refresh),
            'access_token': str(refresh.access_token),
        }


class UserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = User
        fields = (
            'id',
            'username',
            'email',
            'password',
        )


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'created_at',
            'updated_at',
            'number',
            'type',
            'geo',
            'rating',
        )
