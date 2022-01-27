from .client import Client


class LogsException(Exception):
    """Base class for exceptions in this module."""
    pass


class Logs(Client):
    """
    The Event Log API was designed to provide an alternative to the native eth_getLogs.
    """
    def __init__(self, api_key='YourApiKeyToken'):
        Client.__init__(self, address='', api_key=api_key)
        self.url_dict[self.MODULE] = 'logs'
    
    def get_logs(self, from_block: str, to_block='latest', 
                 topic0='', topic1='', topic0_1_opr='and',) -> list:
        """
        Get Event Logs from block number [from_block] to block [to_block] , 
        where log address = [address], topic[0] = [topic0] 'AND' topic[1] = [topic1]

        Args:
            from_block (str): start block number
            to_block (str, optional): end block number. Defaults to 'latest'.
            topic0 (str, optional): Defaults to ''.
            topic1 (str, optional): Defaults to ''.
            topic0_1_opr (str, optional): and|or between topic0 & topic1. Defaults to 'and'.

        Returns:
            list: [description]
        """
        # TODO: support multi topics
        if not topic0 and topic1:
            raise(LogsException('can not only set topic1 while topic0 is empty'))
        self.url_dict[self.ACTION] = 'getLogs'
        self.url_dict[self.FROM_BLOCK] = from_block if type(
            from_block) is str else str(from_block)
        self.url_dict[self.TO_BLOCK] = to_block if type(
            to_block) is str else str(to_block)
        self.url_dict[self.TOPIC0] = topic0 if type(
            topic0) is str else hex(topic0)
        self.url_dict[self.TOPIC1] = topic1 if type(
            topic1) is str else hex(topic1)
        self.url_dict[self.TOPIC0_1_OPR] = topic0_1_opr
        self.build_url()
        req = self.connect()
        return req['result']
