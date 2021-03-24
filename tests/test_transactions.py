import unittest

from etherscan.transactions import Transactions

API_KEY = 'YourAPIkey'
TX_1 = '0x15f8e5ea1079d9a0bb04a4c58ae5fe7654b5b2b4463375ff7ffb490aa0032f3a'
TX_2 = '0x513c1ba0bebf66436b5fed86ab668452b7805593c05073eb2d51d3a52f480a76'
ERROR_STRING = 'Bad jump destination'


class TransactionsTestCase(unittest.TestCase):

    def test_get_status(self):
        api = Transactions(api_key=(API_KEY))
        status = api.get_status(TX_1)
        self.assertEqual(status['isError'], '1')
        self.assertEqual(status['errDescription'], ERROR_STRING)

    def test_get_tx_receipt_status(self):
        api = Transactions(api_key=(API_KEY))
        receipt_status = api.get_tx_receipt_status(TX_2)
        self.assertEqual(receipt_status['status'], '1')
