import re
import unittest

from etherscan.proxies import Proxies

API_KEY = 'YourAPIkey'
BLOCK_NUMBER = 2165403
BLOCK_DIFFICULTY = 67858873048710
UNCLE_INDEX = 0
UNCLE_DIFFICULTY = 67858872000134
TX_COUNT = 4
TX_HASH = "0xed57e2434ddab54526620cbb4dcdaa0c6965027e2cb8556ef4750ed1eafa48c2"
TX_INDEX = 0
TX_ADDRESS = "0x2910543af39aba0cd09dbb2d50200b3e800a63d2"
STORAGE_ADDRESS = "0x6e03d9cce9d60f3e9f2597e13cd4c54c55330cfd"
STORAGE_POS = 0
STORAGE_CONTENTS = "0x0000000000000000000000003d0768d" \
                "a09ce77d25e2d998e6a7b6ed4b9116c2d"
CODE_ADDRESS = "0xf75e354c5edc8efed9b59ee9f67a80845ade7d0c"
CODE_CONTENTS = "0x3660008037602060003660003473273930d21e01ee25e4c219b6" \
                "3259d214872220a261235a5a03f21560015760206000f3"


class ProxiesTestCase(unittest.TestCase):

    def test_get_most_recent_block(self):
        api = Proxies(api_key=API_KEY)
        most_recent = int(api.get_most_recent_block(), 16)
        print(most_recent)
        p = re.compile('^[0-9]{7}$')
        self.assertTrue(p.match(str(most_recent)))

    def test_get_block_by_number(self):
        api = Proxies(api_key=API_KEY)
        block = api.get_block_by_number(BLOCK_NUMBER)
        print(block)
        self.assertEqual(block['difficulty'], hex(BLOCK_DIFFICULTY))

    def test_get_uncle_by_blocknumber_index(self):
        api = Proxies(api_key=API_KEY)
        uncle = api.get_uncle_by_blocknumber_index(BLOCK_NUMBER, UNCLE_INDEX)
        print(uncle)
        self.assertEqual(uncle['difficulty'], hex(UNCLE_DIFFICULTY))

    def test_get_block_transaction_count_by_number(self):
        api = Proxies(api_key=API_KEY)
        tx_count = api.get_block_transaction_count_by_number(BLOCK_NUMBER)
        print(tx_count)
        self.assertEqual(tx_count, hex(TX_COUNT))

    def test_get_transaction_by_hash(self):
        api = Proxies(api_key=API_KEY)
        tx = api.get_transaction_by_hash(TX_HASH)
        print(tx)
        self.assertEqual(tx['blockNumber'], hex(BLOCK_NUMBER))

    def test_get_transaction_by_blocknumber_index(self):
        api = Proxies(api_key=API_KEY)
        tx = api.get_transaction_by_blocknumber_index(BLOCK_NUMBER,
                                                      TX_INDEX)
        print(tx)
        self.assertEqual(tx['hash'], TX_HASH)

    def test_get_transaction_count(self):
        api = Proxies(api_key=API_KEY)
        tx_count = int(api.get_transaction_count(TX_ADDRESS), 16)
        print(tx_count)
        p = re.compile('^[0-9]*$')
        self.assertTrue(p.match(str(tx_count)))

    def test_get_transaction_receipt(self):
        api = Proxies(api_key=API_KEY)
        tx_receipt = api.get_transaction_receipt(TX_HASH)
        print(tx_receipt)
        self.assertEqual(tx_receipt['blockNumber'], hex(BLOCK_NUMBER))

    def test_get_code(self):
        api = Proxies(api_key=API_KEY)
        code_contents = api.get_code(CODE_ADDRESS)
        print(code_contents)
        self.assertEqual(code_contents, CODE_CONTENTS)

    def test_get_storage_at(self):
        api = Proxies(api_key=API_KEY)
        storage_contents = api.get_storage_at(STORAGE_ADDRESS, STORAGE_POS)
        print(storage_contents)
        self.assertEqual(storage_contents, STORAGE_CONTENTS)

    def test_gas_price(self):
        api = Proxies(api_key=API_KEY)
        price = int(api.gas_price(), 16)
        print(price)
        p = re.compile('^[0-9]*$')
        self.assertTrue(p.match(str(price)))
