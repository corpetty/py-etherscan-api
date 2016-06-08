from .client import Client
import json


class Stats(Client):
    def __init__(self):
        Client.__init__(self, address='')
        self.module += 'stats'

    def make_url(self, call_type=''):
        if call_type == 'stats':
            self.url = self.prefix \
                + self.module \
                + self.action \
                + self.key

    def get_total_ether_supply(self):
        self.action += 'ethsupply'
        self.make_url(call_type='stats')
        req = self.connect()
        if req.status_code == 200:
            return json.loads(req.text)['result']
        else:
            return req.status_code

    def get_ether_last_price(self):
        self.action += 'ethprice'
        self.make_url(call_type='stats')
        req = self.connect()
        if req.status_code == 200:
            return json.loads(req.text)['result']
        else:
            return req.status_code
