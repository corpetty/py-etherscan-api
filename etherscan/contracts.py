from .client import Client


class Contract(Client):
    def __init__(self, address=Client.dao_address, api_key='YourApiKeyToken'):
        Client.__init__(self, address=address, api_key=api_key)
        self.module = self.URL_BASES['module'] + 'contract'

    def make_url(self, call_type=''):
        if call_type == 'getabi':
            self.url = self.URL_BASES['prefix'] \
                + self.module \
                + self.action \
                + self.address \
                + self.key

    def get_abi(self):
        self.action = self.URL_BASES['action'] + 'getabi'
        self.make_url(call_type='getabi')
        req = self.connect()
        return req['result']