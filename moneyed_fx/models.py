from django.db import models
from model_utils.models import TimeStampedModel


class FxRate(TimeStampedModel):
    timestamp = models.DateTimeField(db_index=True)
    base_currency = models.CharField(max_length=3)
    rates = models.JSONField()
