# Generated by Django 5.1.7 on 2025-03-08 11:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("book", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="year",
            field=models.SmallIntegerField(),
        ),
    ]
