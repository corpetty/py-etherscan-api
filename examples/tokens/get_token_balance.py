from etherscan.tokens import Tokens

#  tokenname options are:
#     DGD
#     MKR
#     TheDAO
address = '0x0a869d79a7052c7f1b55a8ebabbea3420f0d1e13'
api = Tokens(tokenname='TheDAO')
balance = api.get_token_balance(address=address)
print(balance)
