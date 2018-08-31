import redis
import csv,json
from multiprocessing import Process
import time
from sense_hat import SenseHat
import os
import temperature as temp
import humidity as hum
import paho.mqtt.publish as publish


sense = SenseHat()
redisHost = os.environ['HIVE_HOME']
MQTT_PATH = "datachannel"

r = redis.Redis(
    host=redisHost,
    port=6379,
    password='')

def generateData(message):
    temperature = round(temp.getTempInFarenheit(sense),2)
    humidity = round(hum.getHumidity(sense),2)
    message += redisHost + "," 
    message += str(temperature)
    message += "," + str(humidity)
    return message

def getReading():
    fieldnames=["host","temperature","humidity"]
    message = ""
    message = generateData(message)
    reader = csv.DictReader(message.splitlines(), fieldnames)
    # Parse the CSV into JSON
    out = json.dumps( [ row for row in reader ] )
    return out

def doWork():
    while True:
        jsonValue = getReading()
      
        ips = "" 
        while(True):
          listIPs = r.get("ips")
          if(listIPs != None):
             ips = listIPs 
             break


        ipArray = ips.split(",")
        #Put MQTT publish code here
        for ip in ipArray:
           try:
               publish.single(MQTT_PATH, jsonValue, hostname=ip)
           except:
               print("No running MQTT server on: " + ip)           

        time.sleep(5)

if __name__ == "__main__":
    p = Process(target=doWork)
    p.start()
    while True:
        time.sleep(5)

