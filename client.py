import random
import time
from coapthon.client.helperclient import HelperClient

host = "192.168.1.217"
port = 5683
path = "Temperature"

client = HelperClient(server=(host, port))

percentageLoss = 10
messagesToSend = 100

rand = random.randrange(1,100,1)

startTime = time.time()
for x in range(messagesToSend):
    if rand > percentageLoss:
        response = client.get_non(path)
        print(response.pretty_print())
        print("\n")
    else:
        delay(0.0045)   # To mimic lost packet, delay by average time to deliver and respond to one packet
stopTime = time.time()

timeToDelay = stopTime - startTime
print(timeToDelay)

client.stop()