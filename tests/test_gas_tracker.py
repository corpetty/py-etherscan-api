import unittest
import warnings

from etherscan.gas_tracker import GasTracker

GAS_PRICE = '2000000000'
PRICE_ORACLE_RESULT_DICT_KEYS = ("SafeGasPrice",
                                 "ProposeGasPrice",
                                 "FastGasPrice",
                                 "suggestBaseFee")
API_KEY = 'YourAPIkey'


class BlocksTestCase(unittest.TestCase):

    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        self.api = GasTracker(api_key=API_KEY)

    def test_get_estimation_of_confirmation_time(self):
        estimated_time = self.api.get_estimation_of_confirmation_time(GAS_PRICE)
        self.assertTrue(int(estimated_time) > 0)
    
    def test_get_gas_oracle(self):
        oracle_price = self.api.get_gas_oracle()
        for key in PRICE_ORACLE_RESULT_DICT_KEYS:
            self.assertTrue(key in oracle_price and float(oracle_price[key]) > 0)
