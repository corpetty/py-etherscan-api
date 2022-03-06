from etherscan.proxies import Proxies
import json

with open('../../api_key.json', mode='r') as key_file:
    key = json.loads(key_file.read())['key']

api = Proxies(api_key=key)
price = api.gas_price()
print(price)
