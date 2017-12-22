import re

from etherscan.proxies import Proxies

API_KEY = 'YourAPIkey'


def test_get_most_recent_block():
    api = Proxies(api_key=API_KEY)
    most_recent = int(api.get_most_recent_block(), 16)
    print(most_recent)
    p = re.compile('^[0-9]{7}$')
    assert (p.match(str(most_recent)))
