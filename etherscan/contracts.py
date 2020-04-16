from .client import Client


class Contract(Client):
    def __init__(self, address=Client.dao_address, api_key='YourApiKeyToken'):
        Client.__init__(self, address=address, api_key=api_key)
        self.url_dict[self.MODULE] = 'contract'

    def get_abi(self):
        self.url_dict[self.ACTION] = 'getabi'
        self.build_url()
        req = self.connect()
        return req['result']

    def get_sourcecode(self):
        self.url_dict[self.ACTION] = 'getsourcecode'
        self.build_url()
        req = self.connect()
        return req['result']
