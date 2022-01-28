import os
import sys
import json
import requests
from decouple import config


def binance_contract_address():
    bsc_ca = config('BINANCE_API_KEY')
    bsc_search = input('Enter Binance Contract Address: ')
    response = requests.get(f'https://api.bscscan.com/api?module=contract&action=getsourcecode&address={bsc_search}&apikey={bsc_ca}')
    pretty_json = json.loads(response.text)
    print(json.dumps(pretty_json))




