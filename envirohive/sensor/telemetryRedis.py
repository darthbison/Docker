import redis
import csv,json
from multiprocessing import Process
import time
from sense_hat import SenseHat
import os
import temperature as temp
import humidity as hum
import csv,json

sense = SenseHat()
redisHost = os.environ['HIVE_HOME']

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
        r.set("telemetryReading",jsonValue)
        print(r.get("telemetryReading"))
        time.sleep(5)

if __name__ == "__main__":
    p = Process(target=doWork)
    p.start()
    while True:
        time.sleep(5)

