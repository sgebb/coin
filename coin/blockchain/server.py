import hashlib
import urllib
from threading import Thread
from uuid import uuid4
from flask import Flask
from flask import jsonify
from flask import request

# Instantiate node
app = Flask(__name__)
address = str(uuid4()).replace('-', '')

@app.route('/block', methods=['POST'])
def block():
    global newBlockAppeared
    #look at block
    newBlock = request.get_json()
    last_proof = blockchain.last_block['proof']
    proof = newBlock['proof']

    #making sure all transactions in block are valid
    transactions = newBlock['transactions']
    for transaction in transactions:
        if not blockchain.valid_transaction(transaction):
            transactions.remove(transaction)

    #make sure proof is valid before adding to chain
    if valid_proof(last_proof, proof):
        previous_hash = blockchain.hash(blockchain.last_block)
        blockchain.new_block(proof, previous_hash)
    else:
        return "Bad proof", 400

    blockchain.merge_transactions(transactions)
    block = blockchain.new_block(proof, previous_hash)
    newBlockAppeared = True
    response = {
        'message': "Block accepted",
        'index': block['index'],
        'transactions': block['transactions'],
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


def valid_proof(last_proof, proof):
        guess = (f'{last_proof}{proof}').encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:5] == "00000"


def resolve_conflict(self):
    #TODO 
    neighbors = self.nodes
    new_chain = None

    max_length = len(self.chain)

def notify_peers(block):
    for peer in blockchain.nodes:
        req = urllib.Request('http://127.0.0.1:5000/block')
        print(peer)


def flaskthread():
    print("starting webapp2")
    app.run(host='127.0.0.1', port=5000, threaded=True)


if __name__ == '__main__':
    import coinWithoutServer as coin
    blockchain = coin.BlockChain()
    print("starting webapp")
    p = Thread(target=flaskthread)
    p.start()