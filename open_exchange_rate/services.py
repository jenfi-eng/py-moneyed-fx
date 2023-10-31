from datetime import datetime

from open_exchange_rate.api import Historical, Latest


def get_current_rates(currency):
    response = Latest.for_base(currency)

    return _handle_response(response)


def get_rate_for(currency, date: datetime.date):
    date_str = date.strftime("%Y-%m-%d")

    response = Historical.for_date(date_str, currency)

    return _handle_response(response)


# Some rates don't have enough decimal places like base-VND.
# For example VND -> SGD, look up SGD rate for VND and 1/sgd_vnd to get the reverse rate.
#
# It's a bad assumption to believe it is perfectly inverse, but it's better than truly inaccurate rates.
def use_reverse_rate(currency):
    return currency in ["VND"]


def _handle_response(resp):
    utc_time = datetime.utcfromtimestamp(resp["timestamp"])

    return resp["rates"], utc_time
