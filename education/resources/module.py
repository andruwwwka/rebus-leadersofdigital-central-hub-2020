from rest_framework import serializers, viewsets

from ..models import Module


class ModuleSerializer(serializers.ModelSerializer):
    """Сериализатор для образовательного модуля."""

    class Meta:
        model = Module
        fields = '__all__'


class ModuleViewSet(viewsets.ModelViewSet):
    """Представление для образовательного модуля."""

    queruset = Module.objects.all()
    serializer_class = ModuleSerializer
