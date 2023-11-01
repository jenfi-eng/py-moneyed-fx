# Moneyed FX

This package is built by Jenfi engieering for handling its FX requirements in relation to [py-moneyed](https://github.com/py-moneyed/py-moneyed).

## Requirements

- py-moenyed
- Django

## Quick start

1. **AFTER** `hordak` - Add "moneyed_fx" to your INSTALLED_APPS setting like this::

   INSTALLED_APPS = [
   ...,
   "hordak",
   "moneyed_fx",
   ]

   This app is a monkey patch and needs to be loaded after loading of `moneyed`.

1. Run `python manage.py migrate` to create the polls models.

1. Add a cronjob that runs daily ~4am UTC `moneyed_fx.services.update_all_rates`

## Adding New Exchange Rate Source

- moneyed_fx downloads the rates and saves to the DB.
- Default, it uses `open_exchange_rates.services` as the source.
- must have a module named `services.py`
- Required methods

  - `get_current_rates()`
  - `get_rate_for(currency, date)`
  - Both functions must return the form:

  ```json
  {
    "USD": 451.14,
    "SGD": 1112.12
  }
  ```

- `use_reverse_rates(currency)` - this is unique to OpenExchangeRates and a problem with VND. Return False in most cases.
