# Generated by Django 5.1.4 on 2024-12-09 08:05

from django.db import migrations, models
from django.utils.timezone import now

class Migration(migrations.Migration):

    dependencies = [
        ("boards", "0002_board_date_board_likes_board_reviews_board_writer"),
    ]

    operations = [
        migrations.AddField(
            model_name="board",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, default=now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="board",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]