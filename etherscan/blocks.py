from .client import Client
from typing import Union


class Blocks(Client):
    def __init__(self, api_key='YourApiKeyToken'):
        Client.__init__(self, address='', api_key=api_key)
        self.url_dict[self.MODULE] = 'block'

    def get_block_reward(self, block_number: Union[str, int]):
        self.url_dict[self.ACTION] = 'getblockreward'
        self.url_dict[self.BLOCKNO] = block_number if type(
            block_number) is str else str(block_number)
        self.build_url()
        req = self.connect()
        return req['result']
