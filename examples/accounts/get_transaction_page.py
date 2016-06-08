from etherscan.accounts import Account

address = '0xddbd2b932c763ba5b1b7ae3b362eac3e8d40121a'

api = Account(address=address)
transactions = api.get_transaction_page(page=1, offset=10000, sort='des')
print(transactions)