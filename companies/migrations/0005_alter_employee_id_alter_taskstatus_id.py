# Generated by Django 4.2.4 on 2024-11-26 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("companies", "0004_rename_tasks_task"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employee",
            name="id",
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="taskstatus",
            name="id",
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
