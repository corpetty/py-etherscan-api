from etherscan.stats import Stats
import json

with open('../../api_key.json', mode='r') as key_file:
    key = json.loads(key_file.read())['key']

api = Stats(api_key=key)
last_price = api.get_ether_last_price()
print(last_price)
