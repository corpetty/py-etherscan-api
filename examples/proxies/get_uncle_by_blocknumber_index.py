from  etherscan.proxies import Proxies
import json

with open('../../api_key.json', mode='r') as key_file:
    key = json.loads(key_file.read())['key']

api = Proxies(api_key=key)
uncles = api.get_uncle_by_blocknumber_index(block_number='0x210A9B', index='0x0')
print(uncles['uncles'])