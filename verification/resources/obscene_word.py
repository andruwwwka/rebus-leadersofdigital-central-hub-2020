from rest_framework import serializers, viewsets

from ..models import ObsceneWord


class ObsceneWordSerializer(serializers.ModelSerializer):
    """Сериализатор для нецензурных слов."""

    class Meta:
        model = ObsceneWord
        fields = '__all__'


class ObsceneWordViewSet(viewsets.ModelViewSet):
    """Представление для нецензурных слов."""

    queryset = ObsceneWord.objects.all()
    serializer_class = ObsceneWordSerializer
