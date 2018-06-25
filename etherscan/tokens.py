from .client import Client


class Tokens(Client):
    def __init__(self, contract_address, api_key='YourApiKeyToken'):
        Client.__init__(self, address='', api_key=api_key)
        # self.url_dict[self.TOKEN_NAME] = tokenname
        self.url_dict[self.CONTRACT_ADDRESS] = contract_address

    def get_total_supply(self):
        self.url_dict[self.ACTION] = 'tokensupply'
        self.url_dict[self.MODULE] = 'stats'
        self.build_url()
        req = self.connect()
        return req['result']

    def get_token_balance(self, address):
        self.url_dict[self.ADDRESS] = address
        self.url_dict[self.MODULE] = 'account'
        self.url_dict[self.ACTION] = 'tokenbalance'
        self.build_url()
        req = self.connect()
        return req['result']
