from  etherscan.proxies import Proxies
import json

with open('../../api_key.json', mode='r') as key_file:
    key = json.loads(key_file.read())['key']


api = Proxies(api_key=key)
transaction = api.get_transaction_by_blocknumber_index(block_number='0x57b2cc', index='0x2')
print(transaction['transactionIndex'])