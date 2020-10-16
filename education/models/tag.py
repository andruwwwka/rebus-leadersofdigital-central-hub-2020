from django.db import models


class Tag(models.Model):
    """Модель тэга."""

    key_word = models.CharField(
        max_length=64,
        verbose_name='Ключевое слово'
    )
