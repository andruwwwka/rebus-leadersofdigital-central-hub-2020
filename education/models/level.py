from django.db import models

from .module import Module
from .reference_book import LEVEL_STEPS


class Level(models.Model):
    """Модель уровня."""

    module = models.ManyToManyField(
        Module,
        related_name='levels',
        verbose_name='Модули',
    )

    level_step = models.CharField(
        max_length=2,
        choices=LEVEL_STEPS,
        default='2',
        verbose_name='Уровень',
    )

    target = models.TextField(
        verbose_name='Описание элемента цели',
    )

    example = models.TextField(
        verbose_name='Пример достижения цели (Я могу…)',
    )

