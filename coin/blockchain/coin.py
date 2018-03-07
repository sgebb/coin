import hashlib
import json
from threading import Thread
from time import time
from urllib.parse import urlparse


class BlockChain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.nodes = set()
        self.new_block(previous_hash=1, proof=100)
    
    def new_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1])
        }
        
        self.add_block_to_chain(block)

        return block

    def add_block_to_chain(self, block):
        self.current_transactions = []
        self.chain.append(block)
    
    def new_transaction(self, sender, recipient, amount):
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

        return len(self.chain) +1

    def register_node(self, address):
        parsed_url = urlparse(address)
        self.nodes.add(parsed_url.netloc)

    def merge_transactions(self, transactions):
        for transaction in transactions:
            if not self.current_transactions.__contains__(transaction):
                self.new_transaction(transaction['sender'], transaction['recipient'], transaction['amount'])

    @staticmethod
    def hash(block):
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
        #return hashlib.sha256("aifjaof".encode()).hexdigest()

    @property
    def last_block(self):
        return self.chain[-1]
    
    def valid_chain(self, chain):
        #check if given chain is valid
        last_block = chain[0]
        current_index = 1

        while current_index < len(chain):
            block = chain[current_index]
            print(f'{last_block}')
            print(f'{block}')
            if block['previous_hash'] != self.hash(last_block):
                return False
            
            if not valid_proof(last_block.proof, block['proof']):
                return False
            
            last_block = block
            current_index += 1

        return True

    def valid_transaction(self, transaction):
        return True

def minetask(blockchain, myAddress):
    print("starting minetask")
    proof = proof_of_work(blockchain.last_block['proof'])
    
    if proof is not 0:
        print(f'found the valid proof: {proof}')
        blockchain.new_transaction('0', myAddress, 1)
        blockchain.new_block(proof, blockchain.hash(blockchain.last_block))

shouldBeMining = True

def proof_of_work(last_proof):
        proof = 0
        while valid_proof(last_proof, proof) is False:
            if (shouldBeMining is False):
                return 0
            proof += 1
        return proof

def valid_proof(last_proof, proof):
        guess = (f'{last_proof}{proof}').encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:5] == "00000"


if __name__ == '__main__':

    print("starting mining")

    blockchain = BlockChain()
    mine = Thread(target=minetask, args=(blockchain,"adresse",))
    mine.setDaemon(True)
    mine.start()
    while True:
        while mine.is_alive():
            pass
        mine = Thread(target=minetask, args=(blockchain,"adresse",))
        mine.setDaemon(True)
        mine.start()