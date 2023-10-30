from django.apps import AppConfig


class MoneyedFxConfig(AppConfig):
    name = "moneyed_fx"

    def ready(self):
        from . import moneyed_patches  # noqa: F401s
