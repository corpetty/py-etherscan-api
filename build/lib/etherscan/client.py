import requests
import collections

#  Assume user puts his API key in the api_key.json file under variable name "key"
class Client(object):
    dao_address = '0xbb9bc244d798123fde783fcc1c72d3bb8c189413'

    # Constants
    PREFIX = 'https://api.etherscan.io/api?'
    MODULE = 'module='
    ACTION = '&action='
    CONTRACT_ADDRESS = '&contractaddress='
    ADDRESS = '&address='
    OFFSET = '&offset='
    PAGE = '&page='
    SORT = '&sort='
    BLOCK_TYPE = '&blocktype='
    TO = '&to='
    VALUE = '&value='
    DATA = '&data='
    POSITION = '&='
    HEX = '&hex='
    GAS_PRICE = '&gasPrice='
    GAS = '&gas='
    START_BLOCK = '&startblock='
    END_BLOCK = '&endblock='
    BLOCKNO = '&blockno='
    TXHASH = '&txhash='
    TAG = '&tag='
    BOOLEAN = '&boolean='
    INDEX = '&index='
    API_KEY = '&apikey='

    url_dict = {}

    def __init__(self, address, api_key=''):
        self.http = requests.session()
        self.url_dict = collections.OrderedDict([

            (self.MODULE, ''),
            (self.ADDRESS, ''),
            (self.OFFSET, ''),
            (self.PAGE, ''),
            (self.SORT, ''),
            (self.BLOCK_TYPE, ''),
            (self.TO, ''),
            (self.VALUE, ''),
            (self.DATA, ''),
            (self.POSITION, ''),
            (self.HEX, ''),
            (self.GAS_PRICE, ''),
            (self.GAS, ''),
            (self.START_BLOCK, ''),
            (self.END_BLOCK, ''),
            (self.BLOCKNO, ''),
            (self.TXHASH, ''),
            (self.TAG, ''),
            (self.BOOLEAN, ''),
            (self.INDEX, ''),
            (self.API_KEY, api_key)]
        )

        # self.url_dict[API_KEY] = str(api_key)
        self.check_and_get_api()
        # self.key = self.URL_BASES['key'] + self.API_KEY

        if (len(address) > 20) and (type(address) == list):
            print("Etherscan only takes 20 addresses at a time")
            quit()
        elif (type(address) == list) and (len(address) <= 20):
            self.url_dict[self.ADDRESS] = ','.join(address)
        else:
            self.url_dict[self.ADDRESS] = address

    def build_url(self):
        self.url = self.PREFIX + ''.join([param + val if val else '' for param, val in self.url_dict.items()])

    def connect(self):
        # TODO: deal with "unknown exception" error
        try:
            req = self.http.get(self.url)
        except requests.exceptions.ConnectionError:
            print("Connection refused")
            exit()
            
        if req.status_code == 200:
            # Check for empty response
            if req.text:
                if req.json()['status'] == '1':
                    return req.json()
                else:
                    print(req.json()['message'])
                    exit()
            else:
                print("Invalid Request")
                exit()
        else:
            print("Problem with connection, status code: ", req.status_code)
            exit()

    def check_and_get_api(self):
        if self.url_dict[self.API_KEY]:  # Check if api_key is empty string
            pass
        else:
            self.url_dict[self.API_KEY] = input('Please type your EtherScan.io API key: ')
