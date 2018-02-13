import blockchain.coinWithoutServer as coinWithoutServer
import blockchain.server as server
from threading import Thread
import time

blockchain = coinWithoutServer.BlockChain()
server.blockchain = blockchain
server.newBlockAppeared = False

if __name__ == '__main__':
    print("starting webapp")
    p = Thread(target=server.flaskthread)
    p.start()
    time.sleep(1)

    mine = Thread(target=coinWithoutServer.minetask, args=(blockchain,server.address))
    mine.setDaemon(True)
    mine.start()

    while True:
        while not server.newBlockAppeared and mine.is_alive():
            pass
        if server.newBlockAppeared:
            mine._delete
            print("new block for sure")
            server.newBlockAppeared = False
            #start on new one
        mine = Thread(target=coinWithoutServer.minetask, args=(blockchain,server.address))
        mine.setDaemon(True)
        mine.start()