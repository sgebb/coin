import unittest
import blockchain.coin as coin

class TestCoinMethods(unittest.TestCase):

    def setUp(self):
        self.coin = coin.BlockChain()

class ProofTests(unittest.TestCase):

    def test_valid_proof_genesisProofValid(self):
        self.assertTrue(coin.valid_proof(0, 610536))

    def test_valid_proof_genesisProofInvalid(self):
        self.assertFalse(coin.valid_proof(0, 3511515))

    def test_proof_of_work_genesis(self):
        self.assertEqual(coin.proof_of_work(0), 610536)


if __name__ == '__main__':
    unittest.main()