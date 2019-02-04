from etherscan.blocks import Blocks
import json

with open('../../api_key.json', mode='r') as key_file:
    key = json.loads(key_file.read())['key']

api = Blocks(api_key=key)
reward = api.get_block_reward(5747732)
print(reward)
