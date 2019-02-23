from .client import Client


class Transactions(Client):
    def __init__(self, api_key='YourApiKeyToken'):
        Client.__init__(self, address='', api_key=api_key)
        self.url_dict[self.MODULE] = 'transaction'

    def get_status(self, tx_hash: str):
        self.url_dict[self.ACTION] = 'getstatus'
        self.url_dict[self.TXHASH] = tx_hash
        self.build_url()
        req = self.connect()
        return req['result']

    def get_tx_receipt_status(self, tx_hash: str):
        self.url_dict[self.ACTION] = 'gettxreceiptstatus'
        self.url_dict[self.TXHASH] = tx_hash
        self.build_url()
        req = self.connect()
        return req['result']
