import os
import sys
import json
import requests
from decouple import config


def huobi_contract_address():
    huo_ca = config('HUOBI_API_KEY')
    huo_search = input('Enter Huobi Contract Address: ')
    response = requests.get(f'https://api.hecoinfo.com/api?module=contract&action=getsourcecode&address={huo_search}&apikey={huo_ca}')
    print(response.json())
