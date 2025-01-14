# Generated by Django 5.0.7 on 2024-07-14 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_name', models.CharField(max_length=50)),
                ('video_description', models.CharField(max_length=500)),
                ('video_link', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='onlineclassesmodel',
            name='description',
            field=models.CharField(max_length=500, verbose_name='online_description'),
        ),
    ]
