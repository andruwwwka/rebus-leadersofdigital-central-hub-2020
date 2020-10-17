from rest_framework import serializers, viewsets

from ..models import BanContent


class BanContentSerializer(serializers.ModelSerializer):
    """Сериализатор для запрещенных ресурсов."""

    class Meta:
        model = BanContent
        fields = '__all__'


class BanContentViewSet(viewsets.ModelViewSet):
    """Представление для запрещенных ресурсов."""

    queryset = BanContent.objects.all()
    serializer_class = BanContentSerializer
