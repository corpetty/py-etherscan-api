from .client import Client
import json


class Tokens(Client):
    def __init__(self, tokenname):
        Client.__init__(self, address='')
        self.module += ''
        self.tokenname = '&tokenname=' + tokenname

    def make_url(self, call_type=''):
        if call_type == 'tokensupply':
            self.url = self.prefix \
                + self.module \
                + self.action \
                + self.tokenname \
                + self.key
        elif call_type == 'tokenbalance':
            self.url = self.prefix \
                + self.module \
                + self.action \
                + self.address \
                + self.tokenname \
                + self.key

    def get_total_supply(self):
        self.action += 'tokensupply'
        self.module += 'stats'
        self.make_url(call_type='tokensupply')
        req = self.connect()
        if req.status_code == 200:
            return json.loads(req.text)['result']
        else:
            return req.status_code

    def get_token_balance(self, address):
        self.address += address
        self.module += 'account'
        self.action += 'tokenbalance'
        self.make_url(call_type='tokenbalance')
        req = self.connect()
        if req.status_code == 200:
            return json.loads(req.text)['result']
        else:
            return req.status_code
