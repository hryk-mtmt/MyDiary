# Generated by Django 5.2 on 2025-05-06 13:40

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DiaryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='日付')),
                ('title', models.CharField(max_length=100, verbose_name='タイトル')),
                ('text', models.TextField(verbose_name='本文')),
            ],
        ),
    ]
