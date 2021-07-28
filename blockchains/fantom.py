import os
import sys
import json
import requests
import selenium
from decouple import config


ftm_ca = config('FANTOM_API_KEY')

ftm_search = input('Enter Fantom Contract Address: ')

response = requests.get(f'https://api.ftmscan.com/api?module=contract&action=getsourcecode&address={ftm_search}&apikey={ftm_ca}')


def fantom_contract_address(ftm_ca, response):
    print(response.json())


fantom_contract_address(ftm_ca, response)