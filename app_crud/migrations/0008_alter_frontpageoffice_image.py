# Generated by Django 5.0.1 on 2024-01-10 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_crud', '0007_alter_frontpageoffice_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frontpageoffice',
            name='image',
            field=models.ImageField(upload_to='uploads'),
        ),
    ]
