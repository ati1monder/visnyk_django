# Generated by Django 5.0.7 on 2024-07-17 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0014_offlineclassesmodel_current_participants'),
    ]

    operations = [
        migrations.CreateModel(
            name='ZoomToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_token', models.CharField(max_length=400)),
                ('refresh_token', models.CharField(max_length=400)),
                ('token_expires_str', models.DateField()),
            ],
        ),
    ]