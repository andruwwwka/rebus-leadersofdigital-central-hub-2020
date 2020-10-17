from django.db import models

from .reference_book import TAG_OWNERS


class Tag(models.Model):
    """Модель тэга."""

    key_word = models.CharField(
        max_length=64,
        verbose_name='Ключевое слово',
    )

    owner = models.CharField(
        max_length=16,
        choices=TAG_OWNERS,
        verbose_name='Владелец тэга',
    )
