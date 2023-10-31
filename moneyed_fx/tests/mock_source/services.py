from django.utils import timezone


def get_current_rates():
    return {"USD": 4.0}


def get_rate_for(currency, date):
    return {"USD": 3.0}, timezone.localtime()
