from etherscan.accounts import Account
import json

with open('../../api_key.json', mode='r') as key_file:
    key = json.loads(key_file.read())['key']

#  address = ['0xddbd2b932c763ba5b1b7ae3b362eac3e8d40121a', '0xddbd2b932c763ba5b1b7ae3b362eac3e8d40121a']
address = '0x5bda447c0c2ade0a0b6daf22c88505f9e55f0c61 '

api = Account(address=address, api_key=key)
transactions = api.get_all_transactions(offset=10000, sort='asc')
print(transactions[0])