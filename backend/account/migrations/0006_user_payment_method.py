# Generated by Django 4.1.7 on 2025-01-10 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0005_user_preferred_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="payment_method_id",
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
