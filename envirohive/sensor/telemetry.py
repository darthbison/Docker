#!/usr/bin/python
from sense_hat import SenseHat
import os,sys
import time
import temperature as temp
import humidity as hum
import datetime  

from flask import Flask
import csv,json

sense = SenseHat()

app = Flask(__name__)

def hmsToSeconds(time):
    actualTime = time.split(".")
    h, m, s = [int(i) for i in actualTime[0].split(':')]
    return 3600*h + 60*m + s

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

@app.route('/telemetry')
def tempJSON():
    json = getReading()
    return json

if __name__ == '__main__':
   app.run(host='0.0.0.0',port=8090, debug=True)
