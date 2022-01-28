import os
import sys
import json
import requests
from decouple import config


hs0_ca = config('HARMONY_SHARD_API_KEY')


def harmony_shard_contract_address(hs0_ca):
    input("Enter Harmony Shard Contract Address: ")
