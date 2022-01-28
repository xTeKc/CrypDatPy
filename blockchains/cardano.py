import os
import sys
import json
import requests
from decouple import config


ada_ca = config('CARDANO_API_KEY')


def cardano_contract_address(ada_ca):
    input("Enter Cardano Contract Address: ")
