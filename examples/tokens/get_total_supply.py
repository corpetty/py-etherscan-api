from etherscan.tokens import Tokens
import json

with open('../../api_key.json', mode='r') as key_file:
    key = json.loads(key_file.read())['key']

#  tokenname options are:
#     DGD
#     MKR
#     TheDAO
api = Tokens(tokenname='SNT', api_key=key)
supply = api.get_total_supply()
print(supply)
