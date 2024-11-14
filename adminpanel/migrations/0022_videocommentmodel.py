# Generated by Django 5.0.7 on 2024-07-24 11:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0021_delete_videocommentmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoCommentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=300, verbose_name='Коментар')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminpanel.globalusermodel')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='adminpanel.videomodel')),
            ],
        ),
    ]