from django.db import models


class ObsceneWord(models.Model):
    value = models.CharField(
        verbose_name='Значение непристойного слова',
        max_length=64
    )
