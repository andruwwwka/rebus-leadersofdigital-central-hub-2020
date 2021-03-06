from rest_framework import serializers, viewsets

from ..models import Lesson


class LessonSerializer(serializers.ModelSerializer):
    """Сериализатор для урока."""

    class Meta:
        model = Lesson
        fields = '__all__'


class LessonViewSet(viewsets.ModelViewSet):
    """Представление для урока."""

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
