from rest_framework import serializers, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from verification.models.check import BanContentCheck, ObsceneWordCheck
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
        # task = self.get_object()
        fields_for_check = ('name', 'resources', 'info_for_expert', 'info_for_student', 'info_for_teacher')
        bad_content = []
        bad_words = []
        for field in fields_for_check:
            ban_list = BanContentCheck(request.data[field])
            # bad_word = ObsceneWordCheck(request.data[field])
            bad_content.append({field: ban_list.check_content()})
            # bad_words.append({field: bad_word.check_content()})
        return Response({
            'bad_content': bad_content,
            'bad_words': bad_words
        }, status=200)
