# Generated by Django 4.2.6 on 2024-02-13 08:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("moneyed_fx", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="fxrate",
            name="base_currency",
            field=models.CharField(db_index=True, max_length=3),
        ),
        migrations.AddIndex(
            model_name="fxrate",
            index=models.Index(
                fields=["base_currency", "timestamp"],
                name="base_currency_timestamp_idx",
            ),
        ),
    ]
