from moneyed import Money

from moneyed_fx.services import (
    check_valid_currencies,
    get_current_rate,
    get_stored_rate,
    is_today,
)


def moneyed_fx_test(self):
    return f"Moneyed FX Test: {self}, {self.amount}."


def fx_to(self, to_currency, date_or_datetime=None):
    # Check if to_currency is valid
    check_valid_currencies(self.currency, to_currency)

    # Check if date is None, use
    if date_or_datetime is None or is_today(date_or_datetime):
        rate = get_current_rate(self.currency, to_currency)
    else:
        rate = get_stored_rate(self.currency, to_currency, date_or_datetime)

    # Convert to to_currency with rounding to sub_unit
    fx_ed = Money(self.amount * rate, to_currency)
    ndigits = len(str(fx_ed.currency.sub_unit)) - 1

    return fx_ed.round(ndigits)


Money.moneyed_fx_test = moneyed_fx_test
Money.fx_to = fx_to
