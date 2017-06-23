import requests
import json


#  Assume user puts his API key in the api_key.json file under variable name "key"
class Client(object):
    dao_address = '0xbb9bc244d798123fde783fcc1c72d3bb8c189413'
    URL_BASES = dict(
        prefix='https://api.etherscan.io/',
        module='api?module=',
        action='&action=',
        tag='&tag=',
        offset='&offset=',
        page='&page=',
        sort='&sort=',
        blocktype='&blocktype=',
        key='&apikey=',
        address='&address=',
    )

    def __init__(self, address, api_key='YourApiKeyToken'):
        self.http = requests.session()
        self.url = ''
        self.module = ''
        self.action = ''
        self.tag = ''
        self.offset = ''
        self.page = ''
        self.sort = ''
        self.blocktype = ''

        self.API_KEY = str(api_key)
        self.check_and_get_api()
        self.key = self.URL_BASES['key'] + self.API_KEY
        if (len(address) > 20) and (type(address) == list):
            print("Etherscan only takes 20 addresses at a time")
            quit()
        elif (type(address) == list) and (len(address) <= 20):
            self.address = self.URL_BASES['address'] + ','.join(address)
        else:
            self.address = self.URL_BASES['address'] + address

    def connect(self):
        # TODO: deal with "unknown exception" error
        try:
            req = self.http.get(self.url)
        except requests.exceptions.ConnectionError:
            return "Connection refused"
        if req.status_code == 200:
            # Check for empty response
            if req.text:
                return json.loads(req.text)
            else:
                print("Invalid Request")
                exit()
        else:
            print("problem with connection, status code: ", req.status_code)
            exit()

    def check_and_get_api(self):
        if self.API_KEY != 'YourApiKeyToken':
            pass
        else:
            self.API_KEY = input('Please type your EtherScan.io API key: ')
