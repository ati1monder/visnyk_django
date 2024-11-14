# Generated by Django 5.0.7 on 2024-07-29 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0028_offlineclasssale_onlineclasssale'),
    ]

    operations = [
        migrations.CreateModel(
            name='DayOfOpenedDoors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_enabled', models.BooleanField(verbose_name='Увімкнути/Вимкнути')),
                ('due_to', models.DateField(verbose_name='Кінцеве число')),
            ],
        ),
        migrations.AlterField(
            model_name='subscriptiontypemodel',
            name='duration_in_months',
            field=models.IntegerField(verbose_name='Тривалість'),
        ),
        migrations.AlterField(
            model_name='subscriptiontypemodel',
            name='name',
            field=models.CharField(max_length=20, verbose_name='Назва'),
        ),
        migrations.AlterField(
            model_name='subscriptiontypemodel',
            name='price',
            field=models.IntegerField(verbose_name='Ціна'),
        ),
    ]
