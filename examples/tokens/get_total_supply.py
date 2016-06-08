from etherscan.tokens import Tokens

#  tokenname options are:
#     DGD
#     MKR
#     TheDAO
api = Tokens(tokenname='TheDAO')
supply = api.get_total_supply()
print(supply)
