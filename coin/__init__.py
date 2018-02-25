import blockchain.coinWithoutServer as coinWithoutServer
import blockchain.server as server
from threading import Thread
import time

if __name__ == '__main__':
    blockchain = coinWithoutServer.BlockChain()
    server.blockchain = blockchain
    server.newBlockAppeared = False

    print("starting webapp")
    p = Thread(target=server.flaskthread)
    p.start()
    time.sleep(1)

    mine = Thread(target=coinWithoutServer.minetask, args=(blockchain,server.address))
    mine.setDaemon(True)
    mine.start()

    while True:
        while mine.is_alive():
            if server.newBlockAppeared:
                coinWithoutServer.shouldBeMining = False

        if server.newBlockAppeared:
            print("new block for sure")
            server.newBlockAppeared = False
            #start on new one
        mine = Thread(target=coinWithoutServer.minetask, args=(blockchain,server.address))
        mine.setDaemon(True)
        mine.start()