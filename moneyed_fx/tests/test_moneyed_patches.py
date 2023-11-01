from datetime import timedelta
from decimal import Decimal

from django.test import TestCase, override_settings
from django.utils import timezone
from moneyed import Money

from moneyed_fx.tests.factories import FxRateFactory
from moneyed_fx.tests.mock_source.services import currencies_func


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

    @override_settings(MONEYED_FX_RATE_SOURCE="moneyed_fx.tests.mock_source.services")
    def test_current_rate(self):
        amt = Money(100, "SGD")

        fx_ed = amt.fx_to("USD")

        assert str(fx_ed.currency) == "USD"
        assert fx_ed.amount == 400

    @override_settings(MONEYED_FX_RATE_SOURCE="moneyed_fx.tests.mock_source.services")
    def test_reverse_rate(self):
        amt = Money(100, "VND")

        fx_ed = amt.fx_to("USD")

        assert str(fx_ed.currency) == "USD"
        assert fx_ed.amount == Decimal("25")

    @override_settings(
        CURRENCIES=currencies_func,
        MONEYED_FX_RATE_SOURCE="moneyed_fx.tests.mock_source.services",
    )
    def test_currencies_function(self):
        amt = Money(100, "VND")

        fx_ed = amt.fx_to("USD")

        assert str(fx_ed.currency) == "USD"
        assert fx_ed.amount == Decimal("25")
