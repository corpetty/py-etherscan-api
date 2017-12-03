from .client import Client


class Proxies(Client):
    def __init__(self, api_key='YourApiKeyToken'):
        Client.__init__(self, address='', api_key=api_key)
        self.url_dict[self.MODULE] = 'proxy'

    def get_most_recent_block(self):
        self.url_dict[self.ACTION] = 'eth_blockNumber'
        self.build_url()
        req = self.connect()
        return req['result']
