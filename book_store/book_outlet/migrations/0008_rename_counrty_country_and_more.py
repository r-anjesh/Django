# Generated by Django 5.1.4 on 2025-01-24 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("book_outlet", "0007_counrty_book_published_country"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Counrty",
            new_name="Country",
        ),
        migrations.RenameField(
            model_name="book",
            old_name="published_country",
            new_name="published_countries",
        ),
    ]
