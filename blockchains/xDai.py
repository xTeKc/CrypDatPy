import os
import sys
import json
import requests
from decouple import config


xdai_ca = config('XDAI_API_KEY')


def xdai_contract_address(xdai_ca):
    input("Enter xDai Contract Address: ")
