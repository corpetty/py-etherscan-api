from etherscan.proxies import Proxies
import json

with open('../../api_key.json', mode='r') as key_file:
    key = json.loads(key_file.read())['key']
TX_HASH = '0x1e2910a262b1008d0616a0beb24c1a491d78771baa54a33e66065e03b1f46bc1'
api = Proxies(api_key=key)
transaction = api.get_transaction_by_hash(
    tx_hash=TX_HASH)
print(transaction['hash'])
