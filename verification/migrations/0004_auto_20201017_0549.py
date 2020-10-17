import os

from django.conf import settings
from django.core.management import call_command
from django.db import migrations


def load_obscene_word(apps, schema_editor):
    """Загрузка запрещенных ресурсов."""
    fixture_path = os.path.join(
        settings.BASE_DIR,
        'verification',
        'fixtures',
        'ban_content.json'
    )
    call_command('loaddata', fixture_path)


def remove_obscene_word(apps, schema_editor):
    """Откат загрузки запрещенных ресурсов."""
    apps.get_model('verification', 'BanContent').objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('verification', '0003_bancontent'),
    ]

    operations = [
        migrations.RunPython(load_obscene_word, remove_obscene_word)
    ]
