from rest_framework import serializers, viewsets

from .task import TaskSerializer
from ..models import Module, Level


class ModuleSerializer(serializers.ModelSerializer):
    """Сериализатор для образовательного модуля."""

    class Meta:
        model = Module
        fields = '__all__'


class LevelNestedSerilizer(serializers.ModelSerializer):
    """Вложенный сериализатор для целей."""

    tasks = TaskSerializer(many=True)

    class Meta:
        model = Level
        fields = (
            'level_step',
            'target',
            'example',
            'tasks',
        )


class ModuleDetailSerilizer(ModuleSerializer):
    """Сериализатор для иерархического представления модуля."""

    levels = LevelNestedSerilizer(many=True)

    class Meta:
        model = Module
        fields = (
            'visibility_level',
            'name',
            'version',
            'tags',
            'subject',
            'step',
            'add_module',
            'work_hours',
            'base_idea',
            'problematic_question',
            'general_concept',
            'typical_distribution',
            'possible_difficulties',
            'cover_picture',
            'small_picture',
            'is_active_version',
            'comment',
            'status',
            'owner',
            'levels',
        )


class ModuleViewSet(viewsets.ModelViewSet):
    """Представление для образовательного модуля."""

    queryset = Module.objects.all()
    serializer_class = ModuleSerializer

    def get_serializer_class(self):
        """Класс выбора сериализатора."""
        if self.action == 'retrieve':
            return ModuleDetailSerilizer
        return super().get_serializer_class()
