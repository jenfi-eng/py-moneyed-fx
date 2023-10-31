import datetime as datetime_lib
import importlib
from datetime import datetime, time, timedelta
from decimal import Decimal

from django.conf import settings
from django.utils import timezone

from moneyed_fx.models import FxRate


def get_current_rate(from_currency, to_currency):
    # Get the current rate function
    source_services_mod = _get_rate_source_mod()

    rates = source_services_mod.get_current_rates(from_currency)

    return Decimal(rates[to_currency])


def get_stored_rate(from_currency, to_currency, date_or_datetime):
    rate_datetime = date_or_datetime

    if isinstance(date_or_datetime, datetime_lib.date):
        rate_datetime = _date_to_datetime_in_current_timezone(date_or_datetime)

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


def update_all_rates():
    for currency in settings.CURRENCIES:
        _update_rates_for(currency)


def use_reverse_rates(currency):
    source_services_mod = _get_rate_source_mod()

    return source_services_mod.use_reverse_rate(str(currency))


def check_valid_currencies(from_currency, to_currency):
    if not from_currency.__str__() in settings.CURRENCIES:
        raise ValueError(
            f"Invalid from_currency: {from_currency} not in settings.CURRENCIES"
        )

    if not to_currency.__str__() in settings.CURRENCIES:
        raise ValueError(
            f"Invalid to_currency: {to_currency} not in settings.CURRENCIES"
        )


def is_today(date_or_datetime):
    # Convert datetime to local time
    local_datetime = timezone.localtime(date_or_datetime)

    # Get the current date in local time
    today = timezone.localtime(timezone.now()).date()

    # Compare the dates
    return local_datetime.date() == today


######################################


def _get_rate_source_mod():
    mod_path = getattr(
        settings, "MONEYED_FX_RATE_SOURCE", "open_exchange_rate.services"
    )

    return importlib.import_module(mod_path)


def _date_to_datetime_in_current_timezone(date):
    # Get the current timezone
    current_time = timezone.localtime()

    new_datetime = current_time.replace(
        year=date.year,
        month=date.month,
        day=date.day,
    )

    return new_datetime


########################################


def _update_rates_for(currency):
    latest_rate = (
        FxRate.objects.filter(base_currency=currency).order_by("-timestamp").first()
    )

    if latest_rate is None:
        start_datetime = timezone.now()
        start_datetime = start_datetime.replace(year=2023, month=8, day=1)
    else:
        start_datetime = latest_rate.timestamp

    # Yesterday
    end_date = (timezone.now() - timedelta(days=1)).date()

    current_date = start_datetime.date()

    while current_date <= end_date:
        source_mod = _get_rate_source_mod()

        rates, timestamp = source_mod.get_rate_for(currency, current_date)

        fx_rate, created = FxRate.objects.get_or_create(
            base_currency=currency, timestamp=timestamp, defaults={"rates": rates}
        )

        if not created:
            fx_rate.rates = rates
            fx_rate.save()

        current_date += timedelta(days=1)
