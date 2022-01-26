# Generated by Django 4.0.1 on 2022-01-25 20:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Address",
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
                ("address", models.TextField(max_length=50)),
                ("price", models.IntegerField()),
                ("meters", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="City",
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
                ("name", models.CharField(max_length=20)),
                ("slug", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="Histogram",
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
                ("histogram_price_district", models.ImageField(upload_to="")),
                ("histogram_meters_district", models.ImageField(upload_to="")),
                (
                    "city",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="warm.city"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="District",
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
                ("district", models.TextField(max_length=100)),
                (
                    "address",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="warm.address"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Coordinates",
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
                    "address",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="warm.address"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="address",
            name="city",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="warm.city"
            ),
        ),
    ]
