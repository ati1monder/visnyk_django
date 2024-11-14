# Generated by Django 5.0.7 on 2024-07-15 16:31

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0007_onlineclassesmodel_start_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offlineclassesmodel',
            name='start_time_time',
        ),
        migrations.AddField(
            model_name='offlineclassesmodel',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Дата:'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='offlineclassesmodel',
            name='start_time',
            field=models.TimeField(verbose_name='Час:'),
        ),
        migrations.AlterField(
            model_name='onlineclassesmodel',
            name='zoom_link',
            field=models.CharField(default=None, max_length=255, verbose_name='zoom_link'),
        ),
    ]