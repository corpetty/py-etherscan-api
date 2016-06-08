import requests
from api_key import key


#  Assume user puts his API key in the api_key.py file under variable name "key"
class Client(object):
    dao_address = '0xbb9bc244d798123fde783fcc1c72d3bb8c189413'

    def __init__(self, address):
        self.http = None
        self.url = ''
        self.prefix = 'https://api.etherscan.io/'
        self.module = 'api?module='
        self.action = '&action='
        self.tag = '&tag='
        self.offset = '&offset='
        self.page = '&page='
        self.sort = '&sort='
        self.blocktype = '&blocktype='

        self.key = '&apikey=' + str(key)
        if (len(address) > 20) and (type(address)== list):
            print("Etherscan only takes 20 addresses at a time")
            quit()
        elif (type(address) == list) and (len(address) <= 20):
            self.address = '&address=' + ','.join(address)
        else:
            self.address = '&address=' + address

    def connect(self):
        # TODO: deal with "unknown exception" error
        try:
            req = requests.get(self.url)
        except requests.exceptions.ConnectionError:
            req.status_code = "Connection refused"
        return req
