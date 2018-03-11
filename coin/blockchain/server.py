import hashlib
import blockchain.coin as coin
from threading import Thread
from uuid import uuid4
from flask import Flask
from flask import jsonify
from flask import request
from urllib.parse import urlparse

# Instantiate node
app = Flask(__name__)
address = str(uuid4()).replace('-', '')
nodes = set()

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
    if valid_proof(last_proof, proof) is False:
        return "Bad proof", 400

    #accept new block
    blockchain.add_block_to_chain(newBlock)

    newBlockAppeared = True
    response = {
        'message': "Block accepted",
        'index': newBlock['index'],
        'transactions': newBlock['transactions'],
        'proof': newBlock['proof'],
        'previous_hash': newBlock['previous_hash'],
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

@app.route('/chain', methods=['POST'])
def replace_chain():
    newChain = request.get_json()

    if newChain[0] is not blockchain.chain:
        return "Wrong genesis", 400
    if len(newChain) <= len(blockchain.chain):
        return "Already have a longer or equal length chain", 400
    if not coin.valid_chain(newChain):
        return "Proposed chain not valid", 400

    blockchain.chain = newChain
    return "Chain accepted", 200

#tar inn liste med noder - hver har addresse?
@app.route('/nodes', methods=['POST'])
def addNodes():
    newNodes = request.get_json().get('nodes')
    if newNodes is None:
        return "Error - want list of nodes", 400

    for node in newNodes:
        register_node(node)
    
    response = {
        'message': 'New nodes have been added',
        'total_nodes': list(nodes),
    }
    return jsonify(response), 201


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
    for peer in nodes:
        response = requests.POST(f'http://{peer}/chain')

        if response.status_code == 200:
                length = response.json()['length']
                chain = response.json()['chain']


def flaskthread():
    print("starting webapp")
    app.run(host='127.0.0.1', port=5000, threaded=True)



def register_node(address):
    parsed_url = urlparse(address)
    nodes.add(parsed_url.netloc)


if __name__ == '__main__':
    import coinWithoutServer as coin
    blockchain = coin.BlockChain()
    print("starting webapp")
    p = Thread(target=flaskthread)
    p.start()