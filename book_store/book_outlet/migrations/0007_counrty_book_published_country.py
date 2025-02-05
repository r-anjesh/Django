# Generated by Django 5.1.4 on 2025-01-24 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("book_outlet", "0006_address_author_address"),
    ]

    operations = [
        migrations.CreateModel(
            name="Counrty",
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
                ("name", models.CharField(max_length=10)),
                ("code", models.CharField(max_length=5)),
            ],
        ),
        migrations.AddField(
            model_name="book",
            name="published_country",
            field=models.ManyToManyField(to="book_outlet.counrty"),
        ),
    ]
