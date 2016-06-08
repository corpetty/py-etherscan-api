from .client import Client
import json
import re


class Account(Client):
    def __init__(self, address=Client.dao_address):
        Client.__init__(self, address=address)
        self.module += 'account'

    def make_url(self, call_type=''):
        if call_type == 'balance':
            self.url = self.prefix \
                + self.module \
                + self.action \
                + self.address \
                + self.tag \
                + self.key
        elif call_type == 'transactions':
            self.url = self.prefix \
                + self.module \
                + self.action \
                + self.address \
                + self.offset \
                + self.page \
                + self.key
        elif call_type == 'blocks':
            self.url = self.prefix \
                + self.module \
                + self.action \
                + self.address \
                + self.blocktype \
                + self.offset \
                + self.page \
                + self.key

    def get_balance(self):
        self.action += 'balance'
        self.tag += 'latest'
        self.make_url()
        req = self.connect()
        if req.status_code == 200:
            return json.loads(req.text)['result']
        else:
            return req.status_code

    def get_balance_multiple(self):
        self.action += 'balancemulti'
        self.tag += 'latest'
        self.make_url(call_type='balance')
        req = self.connect()
        if req.status_code == 200:
            return json.loads(req.text)['result']
        else:
            return req.status_code

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
        self.action += 'txlist'
        self.page += str(page)
        self.offset += str(offset)
        self.sort += sort
        self.make_url(call_type='transactions')
        req = self.connect()
        if req.status_code == 200:
            return json.loads(req.text)['result']
        else:
            return req.status_code

    def get_all_transactions(self, offset=10000, sort='asc') -> list:
        self.action += 'txlist'
        self.page += str(1)
        self.offset += str(offset)
        self.sort += sort
        self.make_url(call_type='transactions')

        trans_list = []
        while True:
            self.make_url(call_type='transactions')
            req = self.connect()
            if "No transactions found" in json.loads(req.text)['message']:
                print("Total number of transactions: {}".format(len(trans_list)))
                return trans_list
            else:
                trans_list += json.loads(req.text)['result']
                # Find any character block that is a integer of any length
                page_number = re.findall(r'[1-9](?:\d{0,2})(?:,\d{3})*(?:\.\d*[1-9])?|0?\.\d*[1-9]|0', self.page)
                print("page {} added".format(page_number[0]))
                self.page = self.page[:6] + str(int(page_number[0]) + 1)

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
        self.action += 'getminedblocks'
        self.blocktype += blocktype
        self.page += str(page)
        self.offset += str(offset)
        self.make_url(call_type='blocks')
        req = self.connect()
        if req.status_code == 200:
            return json.loads(req.text)['result']
        else:
            return req.status_code

    def get_all_blocks_mined(self, blocktype='blocks', offset=10000) -> list:
        self.action += 'getminedblocks'
        self.blocktype += blocktype
        self.page += str(1)
        self.offset += str(offset)
        blocks_list = []
        while True:
            self.make_url(call_type='blocks')
            req = self.connect()
            print(json.loads(req.text)['message'])
            if "No transactions found" in json.loads(req.text)['message']:
                print("Total number of blocks mined: {}".format(len(blocks_list)))
                return blocks_list
            else:
                blocks_list += json.loads(req.text)['result']
                # Find any character block that is a integer of any length
                page_number = re.findall(r'[1-9](?:\d{0,2})(?:,\d{3})*(?:\.\d*[1-9])?|0?\.\d*[1-9]|0', self.page)
                print("page {} added".format(page_number[0]))
                self.page = self.page[:6] + str(int(page_number[0]) + 1)

    def update_transactions(self, address, trans):
        """
        Gets last page of transactions (last 10k trans) and updates current trans book (book)
        """
        pass
