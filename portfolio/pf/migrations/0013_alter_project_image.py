# Generated by Django 4.2.7 on 2024-01-01 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pf', '0012_project_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.FileField(blank=True, upload_to='media/'),
        ),
    ]
