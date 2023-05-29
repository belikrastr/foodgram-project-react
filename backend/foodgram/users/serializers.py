from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Follow, User


class CustomUserCreateSerializer(UserCreateSerializer):
    email = serializers.EmailField(
        validators=[
            UniqueValidator(
                message='Указанный email используется другим пользователем!',
                queryset=User.objects.all()
            )
        ]
    )
    username = serializers.CharField(
        validators=[
            UniqueValidator(
                message='Пользователь с указанным именемуже существует!',
                queryset=User.objects.all()
            )
        ]
    )

    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'email': {'required': True},
            'username': {'required': True},
            'password': {'required': True},
            'first_name': {'required': True},
            'last_name': {'required': True},
        }


class CustomUserlistSerializer(UserSerializer):
    is_subscribed = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('email', 'id', 'username', 'first_name',
                  'last_name', 'is_subscribed')

    def get_is_subscribed(self, obj):
        user = self.context.get('request').user
        return user.is_authenticated and Follow.objects.filter(
            user=user, author=obj.id
        ).exists()
