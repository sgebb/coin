import unittest
import blockchain.coinWithoutServer as coinWithoutServer

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

class TestCoinMethods(unittest.TestCase):

    def setUp(self):
        self.coin = coinWithoutServer.BlockChain()

class ProofTests(unittest.TestCase):

    def test_valid_proof_genesisProofValid(self):
        self.assertTrue(coinWithoutServer.valid_proof(0, 610536))

    def test_valid_proof_genesisProofInvalid(self):
        self.assertFalse(coinWithoutServer.valid_proof(0, 3511515))

    def test_proof_of_work_genesis(self):
        self.assertEqual(coinWithoutServer.proof_of_work(0), 610536)


if __name__ == '__main__':
    unittest.main()