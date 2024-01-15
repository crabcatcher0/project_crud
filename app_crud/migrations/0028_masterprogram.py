# Generated by Django 5.0.1 on 2024-01-15 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_crud', '0027_alter_bachelor_id_alter_plus2_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='MasterProgram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_title', models.CharField(default='SomeDefaultTitle', max_length=100)),
                ('course_description', models.CharField(default='SomeDefaultDescription', max_length=2000)),
                ('affiliation', models.CharField(default='TU', max_length=100, null=True)),
                ('duration', models.CharField(default='SomeDefaultDuration', max_length=300)),
                ('eligibility', models.CharField(default='SomeDefaultDuration', max_length=300)),
                ('career', models.CharField(default='DefaultCareer', max_length=1000)),
                ('course_summary', models.CharField(default='DefaultSummary', max_length=2000)),
                ('course_file', models.FileField(blank=True, null=True, upload_to='master_files/')),
            ],
        ),
    ]