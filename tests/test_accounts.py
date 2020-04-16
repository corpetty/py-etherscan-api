import unittest

from etherscan.accounts import Account

SINGLE_BALANCE = '40807178566070000000000'
SINGLE_ACCOUNT = '0xddbd2b932c763ba5b1b7ae3b362eac3e8d40121a'
MULTI_ACCOUNT = [
    '0xddbd2b932c763ba5b1b7ae3b362eac3e8d40121a',
    '0xddbd2b932c763ba5b1b7ae3b362eac3e8d40121a',
]
MULTI_BALANCE = [
    {'account': '0xddbd2b932c763ba5b1b7ae3b362eac3e8d40121a',
     'balance': '40807178566070000000000'},
    {'account': '0xddbd2b932c763ba5b1b7ae3b362eac3e8d40121a',
     'balance': '40807178566070000000000'}
]
API_KEY = 'YourAPIkey'


class AccountsTestCase(unittest.TestCase):

    def test_get_balance(self):
        api = Account(address=SINGLE_ACCOUNT, api_key=API_KEY)
        self.assertEqual(api.get_balance(), SINGLE_BALANCE)

    def test_get_balance_multi(self):
        api = Account(address=MULTI_ACCOUNT, api_key=API_KEY)
        self.assertEqual(api.get_balance_multiple(), MULTI_BALANCE)
