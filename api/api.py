from flask import Flask
from flask_restful import Api, Resource, reqparse
import random
app = Flask(__name__)
api = Api(app)


cryptocurrcies = [
    {
        "id": "uni-eth",
        "name": "uniswap-eth",
        "contract_address": "0x1f9840a85d5af5bf1d1762f925bdaddc4201f984"
    },
    {
        "id": "uni-bsc",
        "name": "uniswap-bsc",
        "contract_address": "0xbf5140a22578168fd562dccf235e5d43a02ce9b1"
    }
]


