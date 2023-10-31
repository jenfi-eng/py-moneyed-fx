from datetime import date, datetime, time
from decimal import Decimal

from django.conf import settings
from django.utils import timezone

from moneyed_fx.models import FxRate


def check_valid_currencies(from_currency, to_currency):
    if not from_currency.__str__() in settings.CURRENCIES:
        raise ValueError(
            f"Invalid from_currency: {from_currency} not in settings.CURRENCIES"
        )

    if not to_currency.__str__() in settings.CURRENCIES:
        raise ValueError(
            f"Invalid to_currency: {to_currency} not in settings.CURRENCIES"
        )


def get_current_rate(from_currency, to_currency):
    # go to the API and ask
    pass


def get_stored_rate(from_currency, to_currency, date_or_datetime):
    rate_datetime = date_or_datetime

    if isinstance(date_or_datetime, date):
        rate_datetime = date_to_datetime_in_current_timezone(date_or_datetime)

    start_of_day = datetime.combine(rate_datetime, time.min)
    end_of_day = datetime.combine(rate_datetime, time.max)

    # go to the database and ask
    rate = (
        FxRate.objects.filter(
            base_currency=from_currency, timestamp__range=(start_of_day, end_of_day)
        )
        .order_by("-timestamp")
        .first()
    )

    return Decimal(rate.rates[to_currency])


def is_today(date_or_datetime):
    # Convert datetime to local time
    local_datetime = timezone.localtime(date_or_datetime)

    # Get the current date in local time
    today = timezone.localtime(timezone.now()).date()

    # Compare the dates
    return local_datetime.date() == today


def date_to_datetime_in_current_timezone(date):
    # Get the current timezone
    current_time = timezone.localtime()

    new_datetime = current_time.replace(
        year=date.year,
        month=date.month,
        day=date.day,
    )

    return new_datetime
