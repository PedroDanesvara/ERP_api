# Generated by Django 4.2.4 on 2024-11-19 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0003_alter_user_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="group",
            name="id",
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
