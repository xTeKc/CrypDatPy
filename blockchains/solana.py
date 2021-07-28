import os
import sys
import json
import requests
import selenium
from decouple import config


sol_ca = config('SOLANA_API_KEY')


def solana_contract_address(sol_ca):
    input("Enter Solana Contract Address: ")
