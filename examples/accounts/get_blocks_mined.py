__author__ = 'Corey Petty'
from etherscan.accounts import Account

address = '0x2a65aca4d5fc5b5c859090a6c34d164135398226'

api = Account(address=address)
blocks = api.get_blocks_mined_page(page=1, offset=10000, blocktype='blocks')
print(blocks)