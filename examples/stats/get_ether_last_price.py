from etherscan.stats import Stats

api = Stats()
last_price = api.get_ether_last_price()
print(last_price)
