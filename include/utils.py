# from requests import request
# import requests
# import time
# import json
# import os
# import dotenv


# URL_BTC = getenv('URL_BTC')
# URL_CURR = getenv('URL_CURR')
# RATIO_CURRENCY = getenv('RATIO_CURRENCY')


# currencies = {
#     "usa": "USD",
#     "canada": "CAD",
#     "europe": "EUR",
#     "britain": "GBP",
#     "new_zeland": "NZD",
#     "turkey": "TRY",
#     "brazil": "BRL",
#     "china": "CNY",
#     "russia": "RUB"
# }
# URL_CURR = 'https://open.er-api.com/v6/latest/'
# URL_BTC = 'https://blockchain.info/ticker'


# def make_req(currencies, url):
#     for i in currencies:
#         response = requests.get(url+currencies[i])
#         res_btc = requests.get(URL_BTC)
#         response_btc = json.loads(res_btc.text)
#         res = json.loads(response.text)
#         row = currencies[i], res['rates'][RATIO_CURRENCY], " - ", "| BTC:", response_btc[currencies[i]]['sell']
#         return row


# def extract_currencies(currencies):
#     from include.models import Snapshot
#     import requests
#     import json
#     cont = []
#     for i in currencies:
#         response = requests.get(URL_CURR+currencies[i])
#         res_btc = requests.get(URL_BTC)
#         response_btc = json.loads(res_btc.text)
#         res = json.loads(response.text)
#         row = {
#             currencies[i]: f"{res['rates'][RATIO_CURRENCY]} | {response_btc[currencies[i]]['sell']}"}
#         cont.append(row)
#     new_snapshot = Snapshot(
#         usa=cont[0]['USD'],
#         canada=cont[1]['CAD'],
#         europe=cont[2]['EUR'],
#         britain=cont[3]['GBP'],
#         new_zeland=cont[4]['NZD'],
#         turkey=cont[5]['TRY'],
#         brazil=cont[6]['BRL'],
#         china=cont[7]['CNY'],
#         russia=cont[8]['RUB'],
#     )
#     NEW_SNAP = new_snapshot
#     print(NEW_SNAP)
#     return NEW_SNAP
