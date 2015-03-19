from twisted.internet import protocol, reactor, endpoints
from twisted.protocols.basic import LineReceiver
import json, time, thread

class Proxy(LineReceiver):
    def connectionMade(self):
        #self.transport.write('whoami')
        print '==> %s ' % 'whoami'

    def dataReceived(self, data):
        self.transport.write(json.dumps({'index':0, 'key':time.time(), 'value':'dsdd'}))

class ProxyFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Proxy()

endpoints.serverFromString(reactor, "tcp:1234").listen(ProxyFactory())
reactor.run()