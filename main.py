import os
import sys
import json
import requests
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
import ui.main_ui as mui


#     binance = blockchains.binance.binance_contract_address()
#     ethereum = blockchains.ethereum.ethereum_contract_address()
#     fantom = blockchains.fantom.fantom_contract_address()
#     huobi = blockchains.huobi.huobi_contract_address()
#     polygon = blockchains.polygon.polygon_contract_address()


#TODO: sort json to only display the contract address
# crypto_contract = {"id": "compound-uniswap", "symbol": "cuni", "name": "cUNI",
# "asset_platform_id": "ethereum", "platforms": {"ethereum": "0x35a18000230da775cac24873d00ff85bccded550"}}


def crypto_info():
    id = input('Enter Crypto ID: ')
    crypto_by_id = requests.get(f'https://api.coingecko.com/api/v3/coins/{id}')
    crypto_data = json.loads(crypto_by_id.text)
    print(json.dumps(crypto_data))

crypto_info()

