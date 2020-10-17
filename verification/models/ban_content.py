from django.db import models


class BanContent(models.Model):
    value = models.CharField(
        verbose_name='URL запрещенного ресурса',
        max_length=254
    )
