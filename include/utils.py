from requests import request
import requests
import time
import json

RATIO = 'RUB'


currencies = {
    "usa": "USD",
    "canada": "CAD",
    "europe": "EUR",
    "britain": "GBP",
    "new zeland": "NZD",
    "turkey": "TRY",
    "norway": "NOK",
    "china": "CNY"
}
URL = 'https://open.er-api.com/v6/latest/'


def make_req(currencies, url):
    for i in currencies:
        response = requests.get(url+currencies[i])
        res = json.loads(response.text)
        print(res['rates'][RATIO])
