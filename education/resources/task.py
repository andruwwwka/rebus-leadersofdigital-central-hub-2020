from rest_framework import serializers, viewsets
from rest_framework.decorators import action

from ..models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Сериализатор для задания."""

    class Meta:
        model = Task
        fields = '__all__'


class TaskViewSet(viewsets.ModelViewSet):
    """Представление для задания."""

    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    @action(methods=['post'], detail=True)
    def кrun_checks(self, request, *args, **kwargs):
        task = self.get_object()
