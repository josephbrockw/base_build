# Generated by Django 4.1.7 on 2024-10-28 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0004_alter_user_email"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="preferred_name",
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
