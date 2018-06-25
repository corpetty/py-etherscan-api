from  etherscan.tokens import Tokens
import json

with open('../../api_key.json', mode='r') as key_file:
    key = json.loads(key_file.read())['key']

address = '0xe04f27eb70e025b78871a2ad7eabe85e61212761'
api = Tokens(contract_address='0x57d90b64a1a57749b0f932f1a3395792e12e7055', api_key=key)
balance = api.get_token_balance(address=address)
print(balance)
