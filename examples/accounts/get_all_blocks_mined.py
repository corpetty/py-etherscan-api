from etherscan.accounts import Account
import json

with open('../../api_key.json', mode='r') as key_file:
    key = json.loads(key_file.read())['key']

address = '0x2a65aca4d5fc5b5c859090a6c34d164135398226'

api = Account(address=address, api_key=key)
blocks = api.get_all_blocks_mined(offset=10000, blocktype='uncles')
print(blocks)