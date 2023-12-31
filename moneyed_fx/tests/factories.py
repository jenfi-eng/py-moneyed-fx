from factory.django import DjangoModelFactory
from factory.faker import Faker

from moneyed_fx.models import FxRate


class FxRateFactory(DjangoModelFactory):
    class Meta:
        model = FxRate

    base_currency = "SGD"
    timestamp = Faker("date_time")
    rates = {
        "AED": 2.745996,
        "AFN": 51.992022,
        "ALL": 82.737593,
        "AMD": 361.243905,
        "ANG": 1.331536,
        "AOA": 124.05465,
        "ARS": 13.900084,
        "AUD": 0.958656,
        "AWG": 1.338312,
        "AZN": 1.271025,
        "BAM": 1.218128,
        "BBD": 1.495323,
        "BDT": 61.768073,
        "BGN": 1.21836,
        "BHD": 0.281277,
        "BIF": 1311.595338,
        "BMD": 0.747662,
        "BND": 0.999613,
        "BOB": 5.17319,
        "BRL": 2.476637,
        "BSD": 0.747662,
        "BTC": 0.00005565158,
        "BTN": 47.645065,
        "BWP": 7.331575,
        "BYN": 1.476475,
        "BZD": 1.500607,
        "CAD": 0.938817,
        "CDF": 1168.506723,
        "CHF": 0.728822,
        "CLF": 0.017234,
        "CLP": 458.682991,
        "CNH": 4.872511,
        "CNY": 4.87539,
        "COP": 2226.27493,
        "CRC": 422.53184,
        "CUC": 0.747662,
        "CUP": 19.065374,
        "CVE": 68.934411,
        "CZK": 15.906335,
        "DJF": 133.509954,
        "DKK": 4.634112,
        "DOP": 36.100225,
        "DZD": 85.80465,
        "EGP": 13.278846,
        "ERN": 11.461654,
        "ETB": 20.457291,
        "EUR": 0.622493,
        "FJD": 1.5237,
        "FKP": 0.55341,
        "GBP": 0.55341,
        "GEL": 1.937687,
        "GGP": 0.55341,
        "GHS": 3.384222,
        "GIP": 0.55341,
        "GMD": 35.635427,
        "GNF": 6734.525589,
        "GTQ": 5.482806,
        "GYD": 154.377193,
        "HKD": 5.842477,
        "HNL": 17.645581,
        "HRK": 4.630269,
        "HTG": 47.675238,
        "HUF": 193.278032,
        "IDR": 10140.870308,
        "ILS": 2.598685,
        "IMP": 0.55341,
        "INR": 47.76078,
        "IQD": 889.886215,
        "IRR": 26638.377614,
        "ISK": 77.328264,
        "JEP": 0.55341,
        "JMD": 92.947917,
        "JOD": 0.531219,
        "JPY": 84.31717701,
        "KES": 77.052507,
        "KGS": 51.929593,
        "KHR": 3032.061122,
        "KMF": 307.038258,
        "KPW": 672.895551,
        "KRW": 797.194312,
        "KWD": 0.225286,
        "KYD": 0.621644,
        "KZT": 248.328582,
        "LAK": 6205.55492,
        "LBP": 1127.875705,
        "LKR": 114.496916,
        "LRD": 93.817736,
        "LSL": 9.178826,
        "LYD": 1.014881,
        "MAD": 6.977612,
        "MDL": 12.766985,
        "MGA": 2437.253813,
        "MKD": 38.343831,
        "MMK": 1010.53822,
        "MNT": 1811.499621,
        "MOP": 6.009263,
        "MRO": 264.880527,
        "MRU": 26.242926,
        "MUR": 25.071272,
        "MVR": 11.514178,
        "MWK": 541.75409,
        "MXN": 14.697684,
        "MYR": 3.036553,
        "MZN": 44.113946,
        "NAD": 9.178245,
        "NGN": 268.051112,
        "NIO": 22.9876,
        "NOK": 6.128613,
        "NPR": 76.281353,
        "NZD": 1.055125,
        "OMR": 0.28785,
        "PAB": 0.747662,
        "PEN": 2.420556,
        "PGK": 2.400016,
        "PHP": 37.323273,
        "PKR": 82.553648,
        "PLN": 2.60036,
        "PYG": 4170.30756,
        "QAR": 2.715171,
        "RON": 2.906536,
        "RSD": 73.587857,
        "RUB": 43.078773,
        "RWF": 641.234478,
        "SAR": 2.804255,
        "SBD": 5.803606,
        "SCR": 10.492311,
        "SDG": 5.231934,
        "SEK": 6.117282,
        "SGD": 1,
        "SHP": 0.55341,
        "SLL": 5720.54676,
        "SOS": 431.264829,
        "SRD": 5.576061,
        "SSP": 97.392958,
        "STD": 15273.79851,
        "STN": 15.273799,
        "SVC": 6.528081,
        "SYP": 385.086901,
        "SZL": 9.183717,
        "THB": 24.351342,
        "TJS": 6.583722,
        "TMT": 2.624273,
        "TND": 1.835885,
        "TOP": 1.692519,
        "TRY": 2.835278,
        "TTD": 5.020735,
        "TWD": 22.269104,
        "TZS": 1679.425706,
        "UAH": 21.019138,
        "UGX": 2716.70967,
        "USD": 0.747662,
        "UYU": 21.552891,
        "UZS": 6057.106685,
        "VEF": 7.465419,
        "VND": 16972.581949,
        "VUV": 78.763671,
        "WST": 1.894351,
        "XAF": 408.328436,
        "XAG": 0.04393881,
        "XAU": 0.00057211,
        "XCD": 2.020593,
        "XDR": 0.524994,
        "XOF": 408.328436,
        "XPD": 0.00069942,
        "XPF": 74.283137,
        "XPT": 0.00080019,
        "YER": 187.155501,
        "ZAR": 9.272338,
        "ZMW": 7.459637,
        "ZWL": 241.012503,
    }
