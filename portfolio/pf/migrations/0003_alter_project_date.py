# Generated by Django 4.2.7 on 2023-12-02 12:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pf", "0002_project_url_alter_project_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="date",
            field=models.DateField(verbose_name="date finished"),
        ),
    ]
