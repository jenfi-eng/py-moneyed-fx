from django.test import TestCase
from moneyed import Money


class TestMoneyedPatches(TestCase):
    def test_basic(self):
        assert 1 == 1
        assert Money(100, "USD").moneyed_fx_test()
