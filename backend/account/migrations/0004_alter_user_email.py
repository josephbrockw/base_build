# Generated by Django 4.1.7 on 2024-10-10 14:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0003_onetimepassword_created"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
