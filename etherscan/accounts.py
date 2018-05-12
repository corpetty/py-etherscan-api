from .client import Client
import re


class Account(Client):
    def __init__(self, address=Client.dao_address, api_key='YourApiKeyToken'):
        Client.__init__(self, address=address, api_key=api_key)
        self.url_dict[self.MODULE] = 'account'

    def get_balance(self):
        self.url_dict[self.ACTION] = 'balance'
        self.url_dict[self.TAG] = 'latest'
        self.build_url()
        req = self.connect()
        return req['result']

    def get_balance_multiple(self):
        self.url_dict[self.ACTION] = 'balancemulti'
        self.url_dict[self.TAG] = 'latest'
        self.build_url()
        req = self.connect()
        return req['result']

    def get_transaction_page(self, page=1, offset=10000, sort='asc', internal=False) -> list:
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
            'desc' -> descending order

        internal options:
            True  -> Gets the internal transactions of a smart contract
            False -> (default) get normal external transactions
        """
        if internal:
            self.url_dict[self.ACTION] = 'txlistinternal'
        else:
            self.url_dict[self.ACTION] = 'txlist'
        self.url_dict[self.PAGE] = str(page)
        self.url_dict[self.OFFSET] = str(offset)
        self.url_dict[self.SORT] = sort
        self.build_url()
        req = self.connect()
        return req['result']

    def get_all_transactions(self, offset=10000, sort='asc', internal=False) -> list:
        if internal:
            self.url_dict[self.ACTION] = 'txlistinternal'
        else:
            self.url_dict[self.ACTION] = 'txlist'
        self.url_dict[self.PAGE] = str(1)
        self.url_dict[self.OFFSET] = str(offset)
        self.url_dict[self.SORT] = sort
        self.build_url()

        trans_list = []
        while True:
            self.build_url()
            req = self.connect()
            if "No transactions found" in req['message']:
                print("Total number of transactions: {}".format(len(trans_list)))
                self.page = ''
                return trans_list
            else:
                trans_list += req['result']
                # Find any character block that is a integer of any length
                page_number = re.findall(r'[1-9](?:\d{0,2})(?:,\d{3})*(?:\.\d*[1-9])?|0?\.\d*[1-9]|0', self.url_dict[self.PAGE])
                print("page {} added".format(page_number[0]))
                self.url_dict[self.PAGE] = str(int(page_number[0]) + 1)

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
        self.url_dict[self.ACTION] = 'getminedblocks'
        self.url_dict[self.BLOCK_TYPE] = blocktype
        self.url_dict[self.PAGE] = str(page)
        self.url_dict[self.OFFSET] = str(offset)
        self.build_url()
        req = self.connect()
        return req['result']

    def get_all_blocks_mined(self, blocktype='blocks', offset=10000) -> list:
        self.url_dict[self.ACTION] = 'getminedblocks'
        self.url_dict[self.BLOCK_TYPE] = blocktype
        self.url_dict[self.PAGE] = str(1)
        self.url_dict[self.OFFSET] = str(offset)
        blocks_list = []
        while True:
            self.build_url()
            req = self.connect()
            print(req['message'])
            if "No transactions found" in req['message']:
                print("Total number of blocks mined: {}".format(len(blocks_list)))
                return blocks_list
            else:
                blocks_list += req['result']
                # Find any character block that is a integer of any length
                page_number = re.findall(r'[1-9](?:\d{0,2})(?:,\d{3})*(?:\.\d*[1-9])?|0?\.\d*[1-9]|0', self.url_dict[self.PAGE])
                print("page {} added".format(page_number[0]))
                self.url_dict[self.PAGE] = str(int(page_number[0]) + 1)

    def get_internal_by_hash(self, tx_hash=''):
        """
        Currently not implemented
        :return:
        """
        pass

    def update_transactions(self, address, trans):
        """
        Gets last page of transactions (last 10k trans) and updates current trans book (book)
        """
        pass
