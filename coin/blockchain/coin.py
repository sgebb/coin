import hashlib
import json
from threading import Thread
from time import time


class BlockChain(object):
    def __init__(self):
        self.chain = []
        self.clear_current_transactions()
        self.new_block(previous_hash=1, proof=100)
    
    def new_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': 0,
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or hash(self.chain[-1])
        }
        
        self.add_block_to_chain(block)

        return block

    def add_block_to_chain(self, block):
        self.chain.append(block)
        self.clear_current_transactions()
    
    def clear_current_transactions(self):
        self.current_transactions = []

    def new_transaction(self, sender, recipient, amount):
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

        return len(self.chain) +1
    
    def valid_transaction(self, transaction):
        return True

    @property
    def last_block(self):
        return self.chain[-1]

    @property
    def genesis(self):
        return self.chain[0]

def hash(block):
    block_string = json.dumps(block, sort_keys=True).encode()
    return hashlib.sha256(block_string).hexdigest()

def valid_chain(chain):
    #check if given chain is valid
    last_block = chain[0]
    current_index = 1

    while current_index < len(chain):
        block = chain[current_index]
        print(f'{last_block}')
        print(f'{block}')
        if block['previous_hash'] != hash(last_block):
            return False
        
        if not valid_proof(last_block['proof'], block['proof']):
            return False
        
        last_block = block
        current_index += 1

    return True

def minetask(blockchain, myAddress):
    print("starting minetask")
    proof = proof_of_work(blockchain.last_block['proof'])
    
    if proof is not 0:
        print(f'found the valid proof: {proof}')
        blockchain.new_transaction('0', myAddress, 1)
        blockchain.new_block(proof, hash(blockchain.last_block))

def proof_of_work(last_proof):
    global shouldBeMining
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