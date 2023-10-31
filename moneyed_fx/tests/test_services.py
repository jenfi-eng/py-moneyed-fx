from datetime import timedelta

from django.test import TestCase, override_settings
from django.utils import timezone

from moneyed_fx.models import FxRate
from moneyed_fx.services import update_all_rates
from moneyed_fx.tests.factories import FxRateFactory


class TestServices(TestCase):
    def setUp(self):
        self.timestamp = timezone.now() - timedelta(days=5)
        self.rate = FxRateFactory(timestamp=self.timestamp, rates={"USD": 5.0})

    @override_settings(MONEYED_FX_RATE_SOURCE="moneyed_fx.tests.mock_source.services")
    def test_updating_rates(self):
        update_all_rates()

        assert FxRate.objects.count() == 6
