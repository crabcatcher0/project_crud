# Generated by Django 5.0.1 on 2024-01-15 10:56

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_crud', '0028_masterprogram'),
    ]

    operations = [
        migrations.AddField(
            model_name='notice',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
