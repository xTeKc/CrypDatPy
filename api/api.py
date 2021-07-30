from flask import Flask
from flask_restful import Api, Resource, reqparse
import random
app = Flask(__name__)
api = Api(app)


class Contract(Resource):
    
    #Get specific Contract by ID or get Random ID if ID not specified
    def get(self, id=0):
        if id == 0:
            return random.choice(cryptocurrencies), 200
        for contract in cryptocurrencies:
            if(contract["id"] == id):
                return contract, 200
        return "Contract not found", 404
    
    #Ability to Add new Contract
    def post(self, id):
      parser = reqparse.RequestParser()
      parser.add_argument("name")
      parser.add_argument("contract")
      params = parser.parse_args()
      for contract in cryptocurrencies:
          if(id == contract["id"]):
              return f"Contract with id {id} already exists", 400
      contract = {
          "id": int(id),
          "name": params["name"],
          "contract": params["contract"]
      }
      cryptocurrencies.append(contract)
      return contract, 201
    
    #Ability to Modify existing Contract
    def put(self, id):
      parser = reqparse.RequestParser()
      parser.add_argument("name")
      parser.add_argument("contract")
      params = parser.parse_args()
      for contract in cryptocurrencies:
          if(id == contract["id"]):
              contract["name"] = params["name"]
              contract["contract"] = params["contract"]
              return contract, 200
      
      contract = {
          "id": id,
          "name": params["name"],
          "contract": params["contract"]
      }
      
      cryptocurrencies.append(contract)
      return contract, 201
  
  
    def delete(self, id):
      global cryptocurrencies
      cryptocurrencies = [contract for contract in cryptocurrencies if contract["id"] != id]
      return f"Contract with id {id} is deleted.", 200
  
  
cryptocurrencies = [
    {
        "id": "uni-eth",
        "name": "uniswap-eth",
        "contract": "0x1f9840a85d5af5bf1d1762f925bdaddc4201f984"
    },
    {
        "id": "uni-bsc",
        "name": "uniswap-bsc",
        "contract": "0xbf5140a22578168fd562dccf235e5d43a02ce9b1"
    }
]


