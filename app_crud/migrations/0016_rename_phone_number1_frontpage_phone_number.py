# Generated by Django 5.0.1 on 2024-01-12 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_crud', '0015_remove_frontpage_facebook_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='frontpage',
            old_name='phone_number1',
            new_name='phone_number',
        ),
    ]
