from .client import Client


class Stats(Client):
    def __init__(self, api_key='YourApiKeyToken'):
        Client.__init__(self, address='', api_key=api_key)
        self.url_dict[self.MODULE] = 'stats'

    def get_total_ether_supply(self):
        self.url_dict[self.ACTION] = 'ethsupply'
        self.build_url()
        req = self.connect()
        return req['result']

    def get_ether_last_price(self):
        self.url_dict[self.ACTION] = 'ethprice'
        self.build_url()
        req = self.connect()
        return req['result']
