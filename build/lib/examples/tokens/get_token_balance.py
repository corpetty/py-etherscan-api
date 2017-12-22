from  etherscan.tokens import Tokens
import json

with open('../../api_key.json', mode='r') as key_file:
    key = json.loads(key_file.read())['key']

address = '0x0a869d79a7052c7f1b55a8ebabbea3420f0d1e13'
api = Tokens(contract_address='0x57d90b64a1a57749b0f932f1a3395792e12e7055', api_key=key)
balance = api.get_token_balance(address=address)
print(balance)
