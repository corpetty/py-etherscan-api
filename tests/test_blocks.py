import unittest

from etherscan.blocks import Blocks

BLOCK = 2165403
BLOCK_REWARD = '5314181600000000000'
UNCLE_INCLUSION_REWARD = '312500000000000000'
API_KEY = 'YourAPIkey'


class BlocksTestCase(unittest.TestCase):

    def test_get_block_reward(self):
        api = Blocks(api_key=(API_KEY))
        reward_object = api.get_block_reward(BLOCK)
        self.assertEqual(reward_object['blockReward'], BLOCK_REWARD)
        self.assertEqual(reward_object['uncleInclusionReward'],
                         UNCLE_INCLUSION_REWARD)
