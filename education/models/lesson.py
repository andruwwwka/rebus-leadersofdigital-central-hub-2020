from django.db import models

from .task import Task


class Lesson(models.Model):
    """Модель урока."""

    theme = models.TextField(
        verbose_name='Тема урока',
    )

    content = models.TextField(
        verbose_name='Содержание урока',
    )

    tasks = models.ManyToManyField(
        Task,
        related_name='lessons',
        blank=True,
        verbose_name='Задания',
    )
