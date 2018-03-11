import blockchain.coin as coin
import blockchain.server as server
from threading import Thread
import time

if __name__ == '__main__':
    blockchain = coin.BlockChain()
    server.blockchain = blockchain

    p = Thread(target=server.flaskthread)
    p.start()
    time.sleep(1)

    while True:
        #setup
        coin.shouldBeMining = True
        server.newBlockAppeared = False
        server.newChainAppeared = False

        mine = Thread(target=coin.minetask, args=(blockchain,server.address))
        mine.setDaemon(True)
        mine.start()

        while mine.is_alive():
            if server.newBlockAppeared:
                coin.shouldBeMining = False
            if server.newChainAppeared:
                coin.shouldBeMining = False
                blockchain = server.blockchain