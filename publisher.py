# Mike Adams
# Iot Project
# 'client.py'

import time
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
   if rc==0:
      print("connected ok")

broker_address="192.168.1.217"
# broker_address="iot.eclipse.org" #use external broker
client = mqtt.Client("P1")                  #create new instance
#client.on_connect=onconnect  #bind call back function
client.connect(broker_address, 1883, 60) #connect to broker
startTime = time.time()
client.loop_start()  #Start loop


packetsToSend = 100
currPacket = "Packet #"

for x in range(packetsToSend):
   currPacket = "Packet " + str(x)
   client.publish("Packet", currPacket, 2, 0)    #publish
   if client.getSendAgain() == 1:
      print("Sending packet again")
      client.publish("Packet", currPacket, 0, 0)    #publish
   client.setSendAgain(0)

client.loop_stop()    #Stop loop
stopTime = time.time()
timetoSend = stopTime-startTime
print(timetoSend)

