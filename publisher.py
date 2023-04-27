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
client.connect(broker_address, 1883)              #connect to broker
client.loop_start()  #Start loop
time.sleep(4) # Wait for connection setup to complete
client.publish("Temperature", "T = 25c", 0, 0)    #publish
client.loop_stop()    #Stop loop

