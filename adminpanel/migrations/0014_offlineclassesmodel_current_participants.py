# Generated by Django 5.0.7 on 2024-07-17 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0013_offlineclassesmodel_registration_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='offlineclassesmodel',
            name='current_participants',
            field=models.IntegerField(default=0, verbose_name='Поточна кількість учасників'),
        ),
    ]
