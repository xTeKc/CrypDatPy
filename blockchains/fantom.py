import os
import sys
import json
import requests
from decouple import config


def fantom_contract_address():
    ftm_ca = config('FANTOM_API_KEY')
    ftm_search = input('Enter Fantom Contract Address: ')
    response = requests.get(f'https://api.ftmscan.com/api?module=contract&action=getsourcecode&address={ftm_search}&apikey={ftm_ca}')
    print(response.json())
