import hashlib
import json
from textwrap import dedent
from time import time
from uuid import uuid4
from flask import request
from flask import Flask
from flask import jsonify
from multiprocessing import Process
from urllib.parse import urlparse
import urllib

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

        self.current_transactions = []
        self.chain.append(block)

        return block
    
    def new_transaction(self, sender, recipient, amount):
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

        return len(self.chain)

    def register_node(self, address):
        parsed_url = urlparse(address)
        self.nodes.add(parsed_url.netloc)
    
    @staticmethod
    def hash(block):
        block_string = json.dumps(block, sort_keys=True).encode()
        #return hashlib.sha256(block_string).hexdigest()
        return hashlib.sha256("aifjaof".encode()).hexdigest()

    @property
    def last_block(self):
        return self.chain[-1]

    def proof_of_work(self, last_proof):
        
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1
        
        return proof

    def valid_proof(self, last_proof, proof):
        guess = (f'{last_proof}{proof}').encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"
    
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
            
            if not self.valid_proof(last_block.proof, block['proof']):
                return False
            
            last_block = block
            current_index += 1

        return True

    
    def resolve_conflict(self):
        
        neighbors = self.nodes
        new_chain = None

        max_length = len(self.chain)

    def valid_transaction(self, transaction):
        return True

# Instantiate node
app = Flask(__name__)

# Generate a globally unique address for this node
node_identifier = str(uuid4()).replace('-', '')

# Instantiate the Blockchain
blockchain = BlockChain()

@app.route('/block', methods=['POST'])
def block():
    #look at block
    newBlock = request.get_json()
    last_proof = blockchain.last_block['proof']
    proof = newBlock['proof']

    #making sure all transactions in block are valid
    transactions = newBlock['transactions']
    for transaction in transactions:
        if not blockchain.valid_transaction(transaction):
            transactions.remove(transaction)
    
    #only add valid transactions to the block
    newBlock['transactions'] = transactions


    #make sure proof is valid before adding to chain
    if(blockchain.valid_proof(last_proof, proof)):
        previous_hash = blockchain.hash(last_block)
        blockchain.new_block(proof, previous_hash)
    else:
        return "Bad proof", 400
    

    block = blockchain.new_block(proof, previous_hash)

    response = {
        'message': "Block accepted",
        'index': block['index'],
        'transactions':block['transactions'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash'],
    }

    return jsonify(response), 200


@app.route('/transactions', methods=['POST'])
def new_transaction():
    values = request.get_json()

    required = ['sender', 'recipient', 'amount']
    if not all(k in values for k in required):
        return "Missing values", 400

    #check valid transaction


    #add to current_block
    index = blockchain.new_transaction(values['sender'], values['recipient'], values['amount'])

    response = {'message' : f"Transaction will be added to Block {index}"}
    return jsonify(response), 201

@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200

def mineTask():
    print("starting minetask")
    proof = blockchain.proof_of_work(blockchain.last_block['proof'])
    print(f'found the valid proof: {proof}')
    blockchain.new_transaction('0', node_identifier, 1)
    new_block = blockchain.new_block(proof, blockchain.hash(blockchain.last_block))
    notify_peers(new_block)

mine = Process(target=mineTask, args=())

def notify_peers(block):
    for peer in blockchain.nodes:
        req = urllib.Request('http://127.0.0.1:5000/block')
        print(peer)



def flaskThread():
    app.run(host='127.0.0.1', port=5000, threaded=True)


if __name__ == '__main__':
    p = Process(target=flaskThread)
    p.start()
    mine.start()
    while True:
        while mine.is_alive():
            pass
        mine = Process(target = mineTask)
        mine.start()