# Generated by Django 5.0.1 on 2024-01-12 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_crud', '0013_delete_latestevent_notice_image_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notice',
            old_name='name',
            new_name='posted_by',
        ),
    ]
