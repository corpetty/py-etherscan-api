from etherscan.accounts import Account
import json

with open('api_key.json', mode='r') as key_file:
    key = json.loads(key_file.read())['key_snowtrace']

address = '0xe027688a57c4A6Fb2708343cF330aaeB8fe594bb'

api = Account(network="avalanche", address=address, api_key=key)
transactions = api.get_transaction_page(page=1, offset=10000, sort='des')
print(transactions)
