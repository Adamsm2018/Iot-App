# Mike Adams
# IoT App Layer Project
# 'client.py'
# COAP Client. Coapthon3 library used. Documentation and examples referenced https://github.com/Tanganelli/CoAPthon. 

import random
import time
from coapthon.client.helperclient import HelperClient

host = "192.168.1.217"      # Addr of server
port = 5683
path = "Temperature"        # Topic

client = HelperClient(server=(host, port))

percentageLoss = 10         # Percentage packet loss
messagesToSend = 100        

rand = random.randrange(1,100,1)    

startTime = time.time()         
for x in range(messagesToSend):                 # Sends 100 messages with a percent chance the packet is not sent
    if rand > percentageLoss:
        response = client.get_non(path)         #get_non() function for non-confirmed transport. get() used for confirmed
        print(response.pretty_print())
        print("\n")
    else:
        delay(0.0045)   # To mimic lost packet, delay by average time to deliver and respond to one packet
stopTime = time.time()

timeToDelay = stopTime - startTime      
print(timeToDelay)

client.stop()
