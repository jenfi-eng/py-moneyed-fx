from django.apps import AppConfig


class MoneyedFxConfig(AppConfig):
    name = "moneyed_fx"
    default_auto_field = "django.db.models.AutoField"

    def ready(self):
        from . import moneyed_patches  # noqa: F401s
