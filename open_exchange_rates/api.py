import json

import requests
from django.conf import settings


class Base:
    base_url = "https://openexchangerates.org/api"

    @classmethod
    def perform_get(cls, endpoint, options=None):
        response = requests.get(
            f"{cls.base_url}/{endpoint}", params=cls._options(options)
        )
        return cls._parse(response.text)

    @staticmethod
    def _parse(json_str):
        return json.loads(json_str)

    @classmethod
    def _options(cls, options):
        config = settings.OPEN_EXCHANGE_RATES
        default_options = {"app_id": config["api_key"]}
        if options:
            default_options.update(options)
        return default_options


class Historical(Base):
    @classmethod
    def for_date(cls, date_str, base_currency):
        return cls.perform_get(f"historical/{date_str}.json", {"base": base_currency})


class Latest(Base):
    @classmethod
    def for_base(cls, base_currency):
        return cls.perform_get("latest.json", {"base": base_currency})
