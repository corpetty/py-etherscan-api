from .client import Client
import re


class Account(Client):
    def __init__(self, address=Client.dao_address, api_key='KMK786MB5AZYQSFS5CW3JQ9AAW4DCX3AX4'):
        Client.__init__(self, address=address, api_key=api_key)
        self.module = self.URL_BASES['module'] + 'account'

    def make_url(self, call_type=''):
        if call_type == 'balance':
            self.url = self.URL_BASES['prefix'] \
                + self.module \
                + self.action \
                + self.address \
                + self.tag \
                + self.key
        elif call_type == 'transactions':
            self.url = self.URL_BASES['prefix'] \
                + self.module \
                + self.action \
                + self.address \
                + self.offset \
                + self.page \
                + self.key
        elif call_type == 'blocks':
            self.url = self.URL_BASES['prefix'] \
                + self.module \
                + self.action \
                + self.address \
                + self.blocktype \
                + self.offset \
                + self.page \
                + self.key

    def get_balance(self):
        self.action = self.URL_BASES['action'] + 'balance'
        self.tag = self.URL_BASES['tag'] + 'latest'
        self.make_url(call_type='transactions')
        req = self.connect()
        return req['result']

    def get_balance_multiple(self):
        self.action = self.URL_BASES['action'] + 'balancemulti'
        self.tag = self.URL_BASES['tag'] + 'latest'
        self.make_url(call_type='balance')
        req = self.connect()
        return req['result']

    def get_transaction_page(self, page=1, offset=10000, sort='asc') -> list:
        """
        Get a page of transactions, each transaction returns list of dict with keys:
            nonce
            hash
            cumulativeGasUsed
            gasUsed
            timeStamp
            blockHash
            value (in wei)
            input
            gas
            isInternalTx
            contractAddress
            confirmations
            gasPrice
            transactionIncex
            to
            from
            isError
            blockNumber

        sort options:
            'asc' -> ascending order
            'des' -> descending order
        """
        self.action = self.URL_BASES['action'] + 'txlist'
        self.page = self.URL_BASES['page'] + str(page)
        self.offset = self.URL_BASES['offset'] + str(offset)
        self.sort = self.URL_BASES['sort'] + sort
        self.make_url(call_type='transactions')
        req = self.connect()
        return req['result']

    def get_all_transactions(self, offset=10000, sort='asc') -> list:
        self.action = self.URL_BASES['action'] + 'txlist'
        self.page = self.URL_BASES['page'] + str(1)
        self.offset = self.URL_BASES['offset'] + str(offset)
        self.sort = self.URL_BASES['sort'] + sort
        self.make_url(call_type='transactions')

        trans_list = []
        while True:
            self.make_url(call_type='transactions')
            req = self.connect()
            if "No transactions found" in req['message']:
                print("Total number of transactions: {}".format(len(trans_list)))
                self.page = ''
                return trans_list
            else:
                trans_list += req['result']
                # Find any character block that is a integer of any length
                page_number = re.findall(r'[1-9](?:\d{0,2})(?:,\d{3})*(?:\.\d*[1-9])?|0?\.\d*[1-9]|0', self.page)
                print("page {} added".format(page_number[0]))
                self.page = self.URL_BASES['page'] + str(int(page_number[0]) + 1)

    def get_blocks_mined_page(self, blocktype='blocks', page=1, offset=10000) -> list:
        """
        Get a page of blocks mined by given address, returns list of dict with keys:
            blockReward (in wei)
            blockNumber
            timeStamp

        blocktype options:
            'blocks' -> full blocks only
            'uncles' -> uncles only
        """
        self.action = self.URL_BASES['action'] + 'getminedblocks'
        self.blocktype = self.URL_BASES['blocktype'] + blocktype
        self.page = self.URL_BASES['page'] + str(page)
        self.offset = self.URL_BASES['offset'] + str(offset)
        self.make_url(call_type='blocks')
        req = self.connect()
        return req['result']

    def get_all_blocks_mined(self, blocktype='blocks', offset=10000) -> list:
        self.action = self.URL_BASES['action'] + 'getminedblocks'
        self.blocktype = self.URL_BASES['blocktype'] + blocktype
        self.page = self.URL_BASES['page'] + str(1)
        self.offset = self.URL_BASES['offset'] + str(offset)
        blocks_list = []
        while True:
            self.make_url(call_type='blocks')
            req = self.connect()
            print(req['message'])
            if "No transactions found" in req['message']:
                print("Total number of blocks mined: {}".format(len(blocks_list)))
                return blocks_list
            else:
                blocks_list += req['result']
                # Find any character block that is a integer of any length
                page_number = re.findall(r'[1-9](?:\d{0,2})(?:,\d{3})*(?:\.\d*[1-9])?|0?\.\d*[1-9]|0', self.page)
                print("page {} added".format(page_number[0]))
                self.page = self.URL_BASES['page'] + str(int(page_number[0]) + 1)

    def update_transactions(self, address, trans):
        """
        Gets last page of transactions (last 10k trans) and updates current trans book (book)
        """
        pass
