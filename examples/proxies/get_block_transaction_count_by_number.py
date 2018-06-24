from  etherscan.proxies import Proxies
import json

with open('../../api_key.json', mode='r') as key_file:
    key = json.loads(key_file.read())['key']


api = Proxies(api_key=key)
tx_count = api.get_block_transaction_count_by_number(block_number='0x10FB78')
print(int(tx_count, 16))