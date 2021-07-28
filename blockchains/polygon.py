import os
import sys
import json
import requests
import selenium
from decouple import config


poly_ca = config('POLYGON_API_KEY')

poly_search = input('Enter Polygon Contract Address: ')

response = requests.get(f'https://api.polygonscan.com/api?module=contract&action=getsourcecode&address={poly_search}&apikey={poly_ca}')


def polygon_contract_address(poly_ca, response):
    print(response.json())


polygon_contract_address(poly_ca, response)