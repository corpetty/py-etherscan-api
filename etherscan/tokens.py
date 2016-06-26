from .client import Client


class Tokens(Client):
    def __init__(self, tokenname='TheDAO', api_key='YourApiKeyToken'):
        Client.__init__(self, address='', api_key=api_key)
        self.tokenname = '&tokenname=' + tokenname

    def make_url(self, call_type=''):
        if call_type == 'tokensupply':
            self.url = self.URL_BASES['prefix'] \
                + self.module \
                + self.action \
                + self.tokenname \
                + self.key
        elif call_type == 'tokenbalance':
            self.url = self.URL_BASES['prefix'] \
                + self.module \
                + self.action \
                + self.tokenname \
                + self.address \
                + self.key

    def get_total_supply(self):
        self.action = self.URL_BASES['action'] + 'tokensupply'
        self.module = self.URL_BASES['module'] + 'stats'
        self.make_url(call_type='tokensupply')
        req = self.connect()
        return req['result']

    def get_token_balance(self, address):
        self.address = self.URL_BASES['address'] + address
        self.module = self.URL_BASES['module'] + 'account'
        self.action = self.URL_BASES['action'] + 'tokenbalance'
        self.make_url(call_type='tokenbalance')
        req = self.connect()
        return req['result']
