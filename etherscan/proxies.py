from .client import Client
from typing import Union


class Proxies(Client):
    def __init__(self, api_key='YourApiKeyToken'):
        Client.__init__(self, address='', api_key=api_key)
        self.url_dict[self.MODULE] = 'proxy'

    def get_most_recent_block(self):
        self.url_dict[self.ACTION] = 'eth_blockNumber'
        self.build_url()
        req = self.connect()
        return req['result']
    
    def get_block_by_number(self, block_number: Union[str, int]):
        self.url_dict[self.ACTION] = 'eth_getBlockByNumber'
        self.url_dict[self.TAG] = block_number if type(block_number) is str else hex(block_number)
        self.url_dict[self.BOOLEAN] = 'true'
        self.build_url()
        req = self.connect()
        return req['result']

    def get_uncle_by_blocknumber_index(self,
        block_number: Union[str, int],
        index: Union[str, int]):
        self.url_dict[self.ACTION] = 'eth_getUncleByBlockNumberAndIndex'
        self.url_dict[self.TAG] = block_number if type(block_number) is str else hex(block_number)
        self.url_dict[self.INDEX] = index if type(index) is str else hex(index)
        self.build_url()
        req = self.connect()
        return req['result']

    def get_block_transaction_count_by_number(self, block_number: Union[str, int]):
        self.url_dict[self.ACTION] = 'eth_getBlockTransactionCountByNumber'
        self.url_dict[self.TAG] = block_number if type(block_number) is str else hex(block_number)
        self.build_url()
        req = self.connect()
        return req['result']

    def get_transaction_by_hash(self, tx_hash: str):
        self.url_dict[self.ACTION] = 'eth_getTransactionByHash'
        self.url_dict[self.TXHASH] = tx_hash
        self.build_url()
        req = self.connect()
        return req['result']

    def get_transaction_by_blocknumber_index(self,
        block_number: Union[str, int],
        index: Union[str, int]):
        self.url_dict[self.ACTION] = 'eth_getTransactionByBlockNumberAndIndex'
        self.url_dict[self.TAG] = block_number if type(block_number) is str else hex(block_number)
        self.url_dict[self.INDEX] = index if type(index) is str else hex(index)
        self.build_url()
        req = self.connect()
        return req['result']

    def get_transaction_count(self, address: str):
        self.url_dict[self.ACTION] = 'eth_getTransactionCount'
        self.url_dict[self.ADDRESS] = address
        self.url_dict[self.TAG] = 'latest'
        self.build_url()
        req = self.connect()
        return req['result']

    def get_transaction_receipt(self, tx_hash: str):
        self.url_dict[self.ACTION] = 'eth_getTransactionReceipt'
        self.url_dict[self.TXHASH] = tx_hash
        self.build_url()
        req = self.connect()
        return req['result']


