# Generated by Django 5.1.4 on 2024-12-09 06:59

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("boards", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="board",
            name="date",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="board",
            name="likes",
            field=models.PositiveBigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="board",
            name="reviews",
            field=models.PositiveBigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="board",
            name="writer",
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]