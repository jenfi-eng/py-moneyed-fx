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

1. Run ``python manage.py migrate`` to create the polls models.

1. Start the development server and visit <http://127.0.0.1:8000/admin/>
   to create a poll (you'll need the Admin app enabled).

1. Visit <http://127.0.0.1:8000/polls/> to participate in the poll.
