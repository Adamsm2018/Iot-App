# Mike Adams
# IoT App Layer Project
# CoAP Server
# 'main.py'
# Using Coapthon3 library. Documentation and examples of library referenced. https://github.com/Tanganelli/CoAPthon

from coapthon.server.coap import CoAP
from example_resource import BasicResource

class CoAPServer(CoAP):
    def __init__(self, host, port):
        CoAP.__init__(self, (host, port))
        self.add_resource('Temperature/', BasicResource())      # Indicates server is ACKing "Temperature" messages

def main():
    server = CoAPServer("192.168.1.217", 5683)          # IP of own machine, not the client. Listening port
    server.listen(10)
    print("Server Shutdown")
    server.close()
    print("Exiting...")

if __name__ == '__main__':
    main()
