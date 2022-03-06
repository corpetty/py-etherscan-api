from etherscan.proxies import Proxies
import json

with open('../../api_key.json', mode='r') as key_file:
    key = json.loads(key_file.read())['key']

api = Proxies(api_key=key)
value = api.get_storage_at('0x6e03d9cce9d60f3e9f2597e13cd4c54c55330cfd', 0x0)
print(value)
