from django.contrib.postgres.fields import ArrayField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import CASCADE

from .reference_book import VISIBILITY_LEVELS, TASK_TYPES, CHECK_TYPES, WORK_TYPES, WAYS, SOFT_SKILLS, \
    LICENCE_TYPES
from .tag import Tag


class Task(models.Model):
    """Модель задания."""
    name = models.CharField(
        max_length=254,
        verbose_name='Наименование задания',
    )

    tags = models.ManyToManyField(
        Tag,
        related_name='tasks',
        blank=True,
        verbose_name='Тэги',
    )

    visibility_level = models.CharField(
        max_length=16,
        choices=VISIBILITY_LEVELS,
        default='personal',
        verbose_name='Уровень видимости',
    )

    task_type = models.CharField(
        max_length=32,
        choices=TASK_TYPES,
        default='educational',
        verbose_name='Тип задания',
    )

    check_type = models.CharField(
        max_length=32,
        choices=CHECK_TYPES,
        blank=True,
        verbose_name='Тип проверки',
    )

    attempts_count = models.PositiveIntegerField(
        validators=[MaxValueValidator(99)],
        default=0,
        verbose_name='Количество попыток',
    )

    work_form = models.CharField(
        max_length=32,
        choices=WORK_TYPES,
        verbose_name='Форма работы',
    )

    way = models.CharField(
        max_length=32,
        choices=WAYS,
        blank=True,
        verbose_name='Способ выполнения',
    )

    work_minute = models.PositiveIntegerField(
        validators=[MinValueValidator(1)],
        verbose_name='Трудоемкость',
    )

    soft_skills = ArrayField(
            base_field=models.CharField(
                choices=SOFT_SKILLS,
                max_length=64,
                verbose_name='Развиваемые мягкие навыки',
            ),
            size=7,
            blank=True,
    )

    owner = models.TextField(
        max_length=512,
        blank=True,
        verbose_name='ФИО автора',
    )

    license = models.CharField(
        choices=LICENCE_TYPES,
        max_length=64,
        blank=True,
        verbose_name='Лицензия',
    )

    resources = models.TextField(
        blank=True,
        verbose_name='Внешние источники информации'
    )

    info_for_expert = models.TextField(
        blank=True,
        verbose_name='Информация для проверяющего'
    )

    info_for_student = models.TextField(
        blank=True,
        verbose_name='Заметка для ученика'
    )

    info_for_teacher = models.TextField(
        blank=True,
        verbose_name='Информация для учителя'
    )

    comment = models.TextField(
        blank=True,
        verbose_name='Комментарий'
    )

    version = models.IntegerField(
        verbose_name='Версия задания',
    )

    is_active_version = models.BooleanField(
        default=True,
        verbose_name='Текушая версия активна',
    )

    level = models.ForeignKey(
        'Level',
        on_delete=CASCADE,
        blank=True,
        verbose_name='Цель/Уровень',
    )
