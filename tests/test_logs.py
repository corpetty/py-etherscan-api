import unittest
import warnings

from etherscan.logs import Logs, LogsException
from etherscan.client import InvalidAPIKey

FROM_BLOCK = 379224
TO_BLOCK = 400000
ADDRESS = '0x33990122638b9132ca29c723bdf037f1a891a70c'
TOPIC0 = '0xf63780e752c6a54a94fc52715dbc5518a3b4c3c2833d301a204226548a2a8545'
TOPIC1 = '0x72657075746174696f6e00000000000000000000000000000000000000000000'
TOPIC0_1_OPR = 'and'
API_KEY = 'YourAPIkey'


class BlocksTestCase(unittest.TestCase):

    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        self.api = Logs(api_key=(API_KEY))
        
    def test_invalid_api_key(self):
        with self.assertRaises(InvalidAPIKey):
            api = Logs(api_key=('invalid' + API_KEY))
            api.get_logs(from_block=FROM_BLOCK, topic0=TOPIC0)

    def test_get_logs_error(self):
        with self.assertRaises(LogsException):
            self.api.get_logs(from_block=FROM_BLOCK, topic1=TOPIC1)

    def test_get_logs_one_topic(self):
        topics = self.api.get_logs(from_block=FROM_BLOCK, topic0=TOPIC0)
        for topic in topics:
            self.assertTrue(TOPIC0 in topic.get('topics', ''))
        
    def test_get_logs_two_topics(self):
        topics = self.api.get_logs(from_block=FROM_BLOCK, topic0=TOPIC0, topic1=TOPIC1)
        for topic in topics:
            self.assertTrue(TOPIC0 in topic.get('topics', '') 
                            and TOPIC1 in topic.get('topics', ''))
