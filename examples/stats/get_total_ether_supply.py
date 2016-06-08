from etherscan.stats import Stats

# call with default address, The DAO
api = Stats()
supply = api.get_total_ether_supply()
print(supply)