import redis
import csv,json
from multiprocessing import Process
import time
from sense_hat import SenseHat
import os,sys
import temperature as temp
import humidity as hum
import datetime
import csv,json
import socket

sense = SenseHat()
r = redis.Redis(
    host='127.0.0.1',
    port=6379,
    password='')

hostName=socket.gethostname()

def generateData(message):
    temperature = round(temp.getTempInFarenheit(sense),2)
    humidity = round(hum.getHumidity(sense),2)
    message += str(temperature)
    message += "," + str(humidity)
    return message

def getReading():
    fieldnames=["temperature","humidity"]
    message = ""
    message = generateData(message)
    reader = csv.DictReader(message.splitlines(), fieldnames)
    # Parse the CSV into JSON
    out = json.dumps( [ row for row in reader ] )
    return out


def doWork():
    while True:
        jsonValue = getReading()
        r.set(hostName,jsonValue)
        time.sleep(5)

if __name__ == "__main__":
    p = Process(target=doWork)
    p.start()
    while True:
        time.sleep(5)

