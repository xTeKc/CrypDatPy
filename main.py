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

blockchains.binance.binance_contract_address()
blockchains.ethereum.ethereum_contract_address()
blockchains.fantom.fantom_contract_address()
blockchains.huobi.huobi_contract_address()