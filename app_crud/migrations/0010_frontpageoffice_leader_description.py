# Generated by Django 5.0.1 on 2024-01-11 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_crud', '0009_alter_frontpageoffice_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='frontpageoffice',
            name='leader_description',
            field=models.CharField(max_length=500, null='We welcome You With Our Heart.'),
            preserve_default='We welcome You With Our Heart.',
        ),
    ]
