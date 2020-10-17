from django.contrib.auth import authenticate
from drf_yasg2.utils import swagger_auto_schema
from rest_framework import serializers
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class LoginSerializer(serializers.Serializer):
    """Сериалайзер для валидации параметров авторизации."""
    email = serializers.EmailField(write_only=True, required=True)
    password = serializers.CharField(max_length=128, write_only=True, required=True)

    def validate(self, data):
        """Валидация авторизационных параметров."""
        email = data.get('email', None)
        password = data.get('password', None)
        user = authenticate(username=email, password=password)
        if user is None:
            raise serializers.ValidationError(
                'Пользователь с таким email или паролем не найден.'
            )
        if not user.is_active:
            raise serializers.ValidationError(
                'Пользователь деактивирован.'
            )
        return {
            'token': user.token,
            'groups': user.groups.values_list('name', flat=True)
        }


class Login(APIView):
    """Авторизация пользователя."""

    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    @swagger_auto_schema(
        request_body=LoginSerializer
    )
    def post(self, request):
        """Метод обработки запроса на авторизацию."""
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data)
