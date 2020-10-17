from rest_framework import serializers, viewsets

from ..models import Level


class LevelSerializer(serializers.ModelSerializer):
    """Сериализатор для уровня."""

    class Meta:
        model = Level
        fields = '__all__'


class LevelViewSet(viewsets.ModelViewSet):
    """Представление для уровня."""

    queryset = Level.objects.all()
    serializer_class = LevelSerializer
