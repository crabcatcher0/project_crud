# Generated by Django 5.0.1 on 2024-01-14 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_crud', '0023_alter_aboutus_options_remove_aboutus_content_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutus',
            options={'verbose_name_plural': 'About Us'},
        ),
    ]