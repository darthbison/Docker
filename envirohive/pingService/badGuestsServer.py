import redis
import csv,json
import paho.mqtt.client as mqtt
import os

MQTT_SERVER = "localhost" 
MQTT_PATH = "hostchannel"

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(MQTT_PATH)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    x = 1
    #print(msg.topic+" "+str(msg.payload))

if __name__ == "__main__":
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(MQTT_SERVER, 1883, 60)
    client.loop_forever() 

