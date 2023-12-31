# Generated by Django 4.2.5 on 2023-12-27 16:24

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="LikePost",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("post_id", models.CharField(max_length=500)),
                ("username", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                ("user", models.CharField(max_length=100)),
                ("image", models.ImageField(upload_to="post_images")),
                ("caption", models.TextField()),
                ("created_at", models.DateTimeField(default=datetime.datetime.now)),
                ("no_of_likes", models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id_user",
                    models.IntegerField(default=0, primary_key=True, serialize=False),
                ),
                ("bio", models.TextField(blank=True, default="")),
                (
                    "profiling",
                    models.ImageField(
                        default="blank-profile-picture.png", upload_to="profile_images"
                    ),
                ),
                ("location", models.CharField(blank=True, default="", max_length=100)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
