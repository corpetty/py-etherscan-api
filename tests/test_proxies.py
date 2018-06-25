import re
import unittest

from etherscan.client import EmptyResponse
from etherscan.proxies import Proxies

API_KEY = 'YourAPIkey'


class ProxiesTestCase(unittest.TestCase):

    def test_get_most_recent_block(self):
        api = Proxies(api_key=API_KEY)
        # currently raises an exception even though it should not, see:
        # https://github.com/corpetty/py-etherscan-api/issues/32
        most_recent = int(api.get_most_recent_block(), 16)
        print(most_recent)
        p = re.compile('^[0-9]{7}$')
        self.assertTrue(p.match(str(most_recent)))
            
