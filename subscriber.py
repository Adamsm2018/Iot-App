# Mike Adams
# Iot Project
# 'subscriber.py'
import time
import paho.mqtt.client as mqtt

def on_message(client, userdata, message):
    print("Received message '" + str(message.payload.decode('utf-8')) + "' on topic '"
        + message.topic + "' with QoS " + str(message.qos))

#client.on_message = on_message

broker_addr = "192.168.1.217"

client = mqtt.Client("P2")
client.connect(broker_addr, 1883)
client.loop_start()  #Start loop

while 1:
    client.on_message = on_message
    time.sleep(4) # Wait for connection setup to complete
    readout = client.subscribe("Packet")
    print(readout)
    print()
#client.loop_stop()    #Stop loop


