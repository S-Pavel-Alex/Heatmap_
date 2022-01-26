# Generated by Django 4.0.1 on 2022-01-26 01:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("warm", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="CoordinateCity",
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
                ("latitude", models.FloatField()),
                ("longitude", models.FloatField()),
                (
                    "city",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="warm.city"
                    ),
                ),
            ],
        ),
    ]