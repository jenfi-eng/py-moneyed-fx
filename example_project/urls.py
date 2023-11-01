"""example_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from datetime import timedelta

from django.contrib import admin
from django.http import HttpResponse
from django.urls import path
from django.utils.timezone import localtime
from django.views import View
from moneyed import Money

from moneyed_fx.services import update_all_rates
from open_exchange_rates.services import get_current_rates, get_rate_for


class TestRunner1(View):
    def get(self, request):
        rates, timestamp = get_current_rates("SGD")

        return HttpResponse(f"{rates} {timestamp}")


class TestRunner2(View):
    def get(self, request):
        rates, timestamp = get_rate_for(
            "SGD", (localtime() - timedelta(weeks=2)).date()
        )

        return HttpResponse(f"{rates} {timestamp}")


class TestUpdate(View):
    def get(self, request):
        update_all_rates()

        return HttpResponse("Updated")


class TestConvert(View):
    def get(self, request):
        # money = Money(1, "USD").fx_to("VND", localtime() - timedelta(weeks=2))
        # return HttpResponse(f"1 USD to VND: {money}")

        money = Money(10000000, "VND").fx_to("USD", localtime() - timedelta(weeks=2))
        return HttpResponse(f"10000000 VND to USD: {money}")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("__test1__", TestRunner1.as_view()),
    path("__test2__", TestRunner2.as_view()),
    path("__update__", TestUpdate.as_view()),
    path("__test__", TestConvert.as_view()),
]
