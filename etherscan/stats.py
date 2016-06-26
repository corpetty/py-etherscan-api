from .client import Client


class Stats(Client):
    def __init__(self, api_key='YourApiKeyToken'):
        Client.__init__(self, address='', api_key=api_key)
        self.module = self.URL_BASES['module'] + 'stats'

    def make_url(self, call_type=''):
        if call_type == 'stats':
            self.url = self.URL_BASES['prefix'] \
                + self.module \
                + self.action \
                + self.key

    def get_total_ether_supply(self):
        self.action = self.URL_BASES['action'] + 'ethsupply'
        self.make_url(call_type='stats')
        req = self.connect()
        return req['result']

    def get_ether_last_price(self):
        self.action = self.URL_BASES['action'] + 'ethprice'
        self.make_url(call_type='stats')
        req = self.connect()
        return req['result']
