# Generated by Django 4.1.4 on 2022-12-20 07:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ppomdm', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='deal',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
