from twisted.internet.protocol import ClientCreator, Protocol, Factory, ClientFactory
from twisted.protocols.basic import LineReceiver
from twisted.internet import reactor
import sys, time, os, json, thread
from twisted.internet.tcp import Client

PORT = 1234
HOST = '192.168.100.24'

messages = []

class MessageQueue:
    lockObj = thread.allocate_lock()
    queue = []

class Cmd(Protocol):
    def __init__(self, queue):
        self.messageQueue = queue

    def dataReceived(self, data):
        messageQueue.lockObj.acquire()
        messageQueue.queue.append(json.loads(data))
        print 'Message:' + data;
        messageQueue.lockObj.release()

class CmdFactory(ClientFactory):

    def __init__(self, queue):
        self.messageQueue = queue
 
    def buildProtocol(self, addr):
        p = Cmd(self.messageQueue)
        p.factory = self
        return p
    def clientConnectionLost(self, connector, reason):
        """If we get disconnected, reconnect to server."""
        #connector.connect()

    def clientConnectionFailed(self, connector, reason):
        print "connection failed:", reason
        reactor.stop()

def runner(id, messageQueue):
    while True:
        msg = {}
        messageQueue.lockObj.acquire()
        print len(messageQueue.queue)
        if(len(messageQueue.queue) > 0):
            msg = messageQueue.queue[0]
        messageQueue.lockObj.release()
        
if __name__ == '__main__':

    messageQueue = MessageQueue()
    f = CmdFactory(messageQueue)
    reactor.connectTCP('192.168.100.24', 1234, f)

    thread.start_new_thread(runner, (0, messageQueue))
    reactor.run()