from rest_framework import serializers, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from ..models import Task
from verification.services import ValidatorRunner


class TaskSerializer(serializers.ModelSerializer):
    """Сериализатор для задания."""

    class Meta:
        model = Task
        fields = '__all__'


class TaskViewSet(viewsets.ModelViewSet):
    """Представление для задания."""

    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    @action(methods=['get'], detail=False)
    def orphans(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset().filter(level__isnull=True))
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['post'], detail=True)
    def run_checks(self, request, pk=None):
        task = self.get_object()
        fields_for_check = (
            'name',
            'resources',
            'info_for_expert',
            'info_for_student',
            'info_for_teacher',
        )
        runner = ValidatorRunner()
        result = {}
        for field in fields_for_check:
            result[field] = runner.run(getattr(task, field))
        return Response(result, status=200)
