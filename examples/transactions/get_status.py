from etherscan.transactions import Transactions
import json

with open('../../api_key.json', mode='r') as key_file:
    key = json.loads(key_file.read())['key']

TX_HASH = '0x15f8e5ea1079d9a0bb04a4c58ae5fe7654b5b2b4463375ff7ffb490aa0032f3a'
api = Transactions(api_key=key)
status = api.get_status(tx_hash=TX_HASH)
print(status)
