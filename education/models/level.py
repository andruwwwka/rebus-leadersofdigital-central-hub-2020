from django.db import models
from django.db.models import CASCADE

from .reference_book import LEVEL_STEPS


class Level(models.Model):
    """Модель уровня."""

    module = models.ForeignKey(
        'Module',
        on_delete=CASCADE,
        verbose_name='Модули',
        related_name='levels',
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
