# Generated by Django 3.1.2 on 2020-10-17 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0006_auto_20201017_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='subject',
            field=models.CharField(blank=True, choices=[('maths', 'Математика'), ('literature', 'Литература'), ('physics', 'Физика'), ('biology', 'Биология'), ('russian', 'Русский язык')], max_length=128, null=True, verbose_name='Предмет'),
        ),
        migrations.AlterField(
            model_name='module',
            name='version',
            field=models.IntegerField(blank=True, null=True, verbose_name='Версия модуля'),
        ),
    ]
