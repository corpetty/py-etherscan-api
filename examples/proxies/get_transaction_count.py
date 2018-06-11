from  etherscan.proxies import Proxies
import json

with open('../../api_key.json', mode='r') as key_file:
    key = json.loads(key_file.read())['key']


api = Proxies(api_key=key)
count = api.get_transaction_count('0x6E2446aCfcec11CC4a60f36aFA061a9ba81aF7e0')
print(int(count, 16))