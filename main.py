import os
import sys
import json
import requests
import selenium
from decouple import config
import blockchains.binance
import blockchains.cardano
import blockchains.ethereum
import blockchains.fantom
import blockchains.harmonyShard
import blockchains.huobi
import blockchains.polygon
import blockchains.solana
import blockchains.xDai


#     binance = blockchains.binance.binance_contract_address()
#     ethereum = blockchains.ethereum.ethereum_contract_address()
#     fantom = blockchains.fantom.fantom_contract_address()
#     huobi = blockchains.huobi.huobi_contract_address()
#     polygon = blockchains.polygon.polygon_contract_address()


def coin_info():
    id = input('Enter Crypto ID: ')
    coin_by_id = requests.get(f'https://api.coingecko.com/api/v3/coins/{id}')
    coin_info = json.loads(coin_by_id.text)
    print(json.dumps(coin_info))

coin_info()



