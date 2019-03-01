from etherscan.proxies import Proxies
import json

with open('../../api_key.json', mode='r') as key_file:
    key = json.loads(key_file.read())['key']

api = Proxies(api_key=key)
code = api.get_code('0xf75e354c5edc8efed9b59ee9f67a80845ade7d0c')
print(code)
