from etherscan.transactions import Transactions
import json

with open('../../api_key.json', mode='r') as key_file:
    key = json.loads(key_file.read())['key']

TX_HASH = '0x513c1ba0bebf66436b5fed86ab668452b7805593c05073eb2d51d3a52f480a76'
api = Transactions(api_key=key)
receipt_status = api.get_tx_receipt_status(tx_hash=TX_HASH)
print(receipt_status)
