from django.utils import timezone


def get_current_rates(currency):
    return {"USD": 4.0, "VND": 4.0}


def get_rate_for(currency, date):
    return {"USD": 3.0}, timezone.localtime()


def use_reverse_rate(currency):
    return currency in ["VND"]
