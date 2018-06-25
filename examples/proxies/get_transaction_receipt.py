from  etherscan.proxies import Proxies
import json

with open('../../api_key.json', mode='r') as key_file:
    key = json.loads(key_file.read())['key']

api = Proxies(api_key=key)
receipt = api.get_transaction_receipt('0xb03d4625fd433ad05f036abdc895a1837a7d838ed39f970db69e7d832e41205d')
print(receipt)