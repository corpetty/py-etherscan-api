__author__ = 'Corey Petty'
from etherscan.accounts import Account

address = ['0xddbd2b932c763ba5b1b7ae3b362eac3e8d40121a', '0xddbd2b932c763ba5b1b7ae3b362eac3e8d40121a']

api = Account(address=address)
balances = api.get_balance_multiple()
print(balances)
