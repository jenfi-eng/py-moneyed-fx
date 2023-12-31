from moneyed import Money

from moneyed_fx.services import (
    check_valid_currencies,
    get_current_rate,
    get_stored_rate,
    is_today,
    use_reverse_rates,
)


def moneyed_fx_test(self):
    return f"Moneyed FX Test: {self}, {self.amount}."


def fx_to(self, to_currency, date_or_datetime=None):
    from_currency = str(self.currency)

    # Check if to_currency is valid
    check_valid_currencies(self.currency, to_currency)

    if use_reverse_rates(self.currency):
        rate = _reverse_rate(from_currency, to_currency, date_or_datetime)
    else:
        rate = _normal_rate(from_currency, to_currency, date_or_datetime)

    # Convert to to_currency with rounding to sub_unit
    return _perform_fx(self, to_currency, rate)


Money.moneyed_fx_test = moneyed_fx_test
Money.fx_to = fx_to


def _reverse_rate(from_currency, to_currency, date_or_datetime):
    if date_or_datetime is None or is_today(date_or_datetime):
        return 1 / get_current_rate(to_currency, from_currency)
    else:
        return 1 / get_stored_rate(to_currency, from_currency, date_or_datetime)


def _normal_rate(from_currency, to_currency, date_or_datetime):
    if date_or_datetime is None or is_today(date_or_datetime):
        return get_current_rate(from_currency, to_currency)
    else:
        return get_stored_rate(from_currency, to_currency, date_or_datetime)


def _perform_fx(self, to_currency, rate):
    fx_ed = Money(self.amount * rate, to_currency)
    ndigits = len(str(fx_ed.currency.sub_unit)) - 1

    return fx_ed.round(ndigits)
