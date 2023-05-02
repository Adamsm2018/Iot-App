# Mike Adams
# Iot Project
# 'subscriber.py'
# Paho mqtt library used. See documentation https://pypi.org/project/paho-mqtt/

import time
import paho.mqtt.client as mqtt

def on_message(client, userdata, message):          # Interupt for when message from broker recieved. 
    print("Received message '" + str(message.payload.decode('utf-8')) + "' on topic '"
        + message.topic + "' with QoS " + str(message.qos))

#client.on_message = on_message

broker_addr = "192.168.1.217"       # IP of broker

client = mqtt.Client("P2")          # Process id for broker
client.connect(broker_addr, 1883)
client.loop_start()  #Start loop

while 1:                                # loop to subscribe to broker every 4 seconds. Unnecesseary but it works so I didnt change it
    client.on_message = on_message
    time.sleep(4) # Wait for connection setup to complete
    readout = client.subscribe("Packet")        # Subscribes to packet topic. Topic is called packet so I could keep track of which packet was being corrupted
    print(readout)
    print()
#client.loop_stop()    #Stop loop


