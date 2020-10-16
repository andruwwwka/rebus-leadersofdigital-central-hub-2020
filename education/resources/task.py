from rest_framework import serializers, viewsets

from ..models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Сериализатор для задания."""

    class Meta:
        model = Task
        fields = '__all__'


class TaskViewSet(viewsets.ModelViewSet):
    """Представление для задания."""

    queryset = Task.objects.all()
    serializer = TaskSerializer
