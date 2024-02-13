from django.db import models
from model_utils.models import TimeStampedModel


class FxRate(TimeStampedModel):
    timestamp = models.DateTimeField(db_index=True)
    base_currency = models.CharField(max_length=3, db_index=True)
    rates = models.JSONField()

    class Meta:
        indexes = [
            models.Index(
                fields=["base_currency", "timestamp"],
                name="base_currency_timestamp_idx",
            ),
        ]
