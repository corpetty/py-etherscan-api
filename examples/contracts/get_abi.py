from etherscan.contracts import Contract
import json

with open('../../api_key.json', mode='r') as key_file:
    key = json.loads(key_file.read())['key']

address = '0xfb6916095ca1df60bb79ce92ce3ea74c37c5d359'

api = Contract(address=address, api_key=key)
abi = api.get_abi()
print(abi)
