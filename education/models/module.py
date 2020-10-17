from django.core.validators import MinValueValidator
from django.db import models

from .reference_book import VISIBILITY_LEVELS, SUBJECTS, STEPS, STATUSES
from .tag import Tag


class Module(models.Model):
    """Модель учебного модуля."""

    visibility_level = models.CharField(
        max_length=16,
        choices=VISIBILITY_LEVELS,
        default='personal',
        verbose_name='Уровень видимости',
    )

    name = models.CharField(
        max_length=254,
        verbose_name='Наименование модуля',
    )

    version = models.IntegerField(
        verbose_name='Версия модуля',
    )

    tags = models.ManyToManyField(
        Tag,
        related_name='modules',
        blank=True,
        verbose_name='Тэги',
    )

    subject = models.CharField(
        max_length=128,
        choices=SUBJECTS,
        verbose_name='Предмет',
    )

    step = models.CharField(
        max_length=128,
        choices=STEPS,
        verbose_name='Класс',
    )

    add_module = models.BooleanField(
        default=False,
        blank=True,
        verbose_name='Дополнительный модуль',
    )

    work_hours = models.PositiveIntegerField(
        validators=[MinValueValidator(1)],
        verbose_name='Трудоемкость',
    )

    base_idea = models.TextField(
        verbose_name='Базовая идея',
    )

    problematic_question = models.TextField(
        verbose_name='Проблемный вопрос',
    )

    general_concept = models.TextField(
        blank=True,
        verbose_name='Общий замысел модуля',
    )

    typical_distribution = models.TextField(
        blank=True,
        verbose_name='Типовое распределение заданий по урокам',
    )

    possible_difficulties = models.TextField(
        blank=True,
        verbose_name='Возможные трудности, ложные представления и способы их преодоления',
    )

    cover_picture = models.FileField(
        blank=True,
        verbose_name='Обложка модуля',
    )

    small_picture = models.FileField(
        blank=True,
        verbose_name='Картинка для списка',
    )

    is_active_version = models.BooleanField(
        default=True,
        verbose_name='Текушая версия активна',
    )

    comment = models.TextField(
        blank=True,
        verbose_name='Комментарий'
    )

    status = models.CharField(
        max_length=32,
        choices=STATUSES,
        default='draft',
        verbose_name='Статус модуля',
    )
