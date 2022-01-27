from .client import Client


class GasTrackerException(Exception):
    """Base class for exceptions in this module."""
    pass


class GasTracker(Client):
    def __init__(self, api_key='YourApiKeyToken'):
        Client.__init__(self, address='', api_key=api_key)
        self.url_dict[self.MODULE] = 'gastracker'
        
    def get_estimation_of_confirmation_time(self, gas_price: str) -> str:
        """
        Returns the estimated time, in seconds, for a transaction to be confirmed on the blockchain.

        Args:
            gas_price (str): the price paid per unit of gas, in wei

        Returns:
            str: The result is returned in seconds.
        """
        self.url_dict[self.ACTION] = 'gasestimate'
        self.url_dict[self.GAS_PRICE] = gas_price
        self.build_url()
        req = self.connect()
        return req['result']
    
    def get_gas_oracle(self) -> dict:
        """
        Returns the current Safe, Proposed and Fast gas prices.

        Returns:
            dict: The gas prices are returned in Gwei.
        """
        self.url_dict[self.ACTION] = 'gasoracle'
        self.build_url()
        req = self.connect()
        return req['result']
    
    def get_daily_average_gas_limit(self, start_date, end_date) -> list:
        # TODO API Pro
        pass
