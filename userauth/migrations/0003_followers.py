# Generated by Django 4.2.5 on 2023-12-28 11:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("userauth", "0002_rename_profiling_profile_profileimg"),
    ]

    operations = [
        migrations.CreateModel(
            name="Followers",
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
                ("follower", models.CharField(max_length=50)),
            ],
        ),
    ]
