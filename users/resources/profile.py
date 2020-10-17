from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    """Сериализатор профиля пользователя."""

    birthday = serializers.DateField(format="%d.%m.%Y")

    class Meta:
        model = Profile
        fields = '__all__'


class Profiles(APIView):
    """Информация профиля для личного кабинета."""
    serializer_class = ProfileSerializer

    def get(self, request):
        """Получение профиля пользователя."""
        profile = request.user
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)
