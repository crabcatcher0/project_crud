# Generated by Django 5.0.1 on 2024-01-10 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_crud', '0004_alter_frontpage_facebook_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frontpage',
            name='phone_number1',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]