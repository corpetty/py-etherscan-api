import unittest

from etherscan.tokens import Tokens

ELCOIN_TOKEN_SUPPLY = '21265524714464'
ELCOIN_TOKEN_BALANCE = "135499"
CONTRACT_ADDRESS = '0x57d90b64a1a57749b0f932f1a3395792e12e7055'
ADDRESS = '0xe04f27eb70e025b78871a2ad7eabe85e61212761'
API_KEY = 'YourAPIkey'


class ProxiesTestCase(unittest.TestCase):

    def test_get_token_supply(self):
        api = Tokens(contract_address=CONTRACT_ADDRESS, api_key=(API_KEY))
        self.assertEqual(api.get_total_supply(), ELCOIN_TOKEN_SUPPLY)

    def test_get_token_balance(self):
        api = Tokens(contract_address=CONTRACT_ADDRESS, api_key=API_KEY)
        self.assertEqual(api.get_token_balance(ADDRESS), ELCOIN_TOKEN_BALANCE)
