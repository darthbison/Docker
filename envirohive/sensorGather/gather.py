import redis
import csv,json
import paho.mqtt.client as mqtt
import os

Host = os.environ['HIVE_HOME']

MQTT_SERVER = Host 
MQTT_PATH = "datachannel"


r = redis.Redis(
    host=Host,
    port=6379,
    password='')

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(MQTT_PATH)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    json = msg.payload

    jsonString = json
    jsonString = jsonString.translate(None,'[]')

    data = Payload(jsonString) 
    host = data.host
    host = host.encode('ascii','ignore')
    host = host.translate(None,'.')

    hostId = "host" + host
    r.set(hostId, json)
    print(r.get(hostId)) 
    # more callbacks, etc

class Payload(object):
     def __init__(self, j):
         self.__dict__ = json.loads(j)


if __name__ == "__main__":
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(MQTT_SERVER, 1883, 60)
    client.loop_forever() 

