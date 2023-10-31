from datetime import timedelta

from django.test import TestCase
from django.utils import timezone
from moneyed import Money

from moneyed_fx.tests.factories import FxRateFactory


class TestMoneyedPatches(TestCase):
    def setUp(self):
        self.timestamp = timezone.now() - timedelta(days=1)
        self.rate = FxRateFactory(timestamp=self.timestamp, rates={"USD": 5.0})

    def test_basic(self):
        assert 1 == 1
        assert Money(100, "USD").moneyed_fx_test() == "Moneyed FX Test: $100.00, 100."

    def test_stored_rate(self):
        amt = Money(100, "SGD")

        fx_ed = amt.fx_to("USD", self.timestamp)

        assert str(fx_ed.currency) == "USD"
        assert fx_ed.amount == 500
