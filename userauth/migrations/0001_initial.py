# Generated by Django 4.2.5 on 2023-12-22 05:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
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
