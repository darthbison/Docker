#!/usr/bin/python
from sense_hat import SenseHat
import os,sys
import time
import temperature as temp
import humidity as hum
import datetime  

sense = SenseHat()
sense.show_message("reading...")
sense.clear()  # Blank the LED matrix


def hmsToSeconds(time):
  actualTime = time.split(".")
  h, m, s = [int(i) for i in actualTime[0].split(':')]
  return 3600*h + 60*m + s

def generateData(message):

    temperature = str(temp.getTempInFarenheit(sense))
    humidity = str(hum.getHumidity(sense))

    message += temperature
    message += "," + humidity
    return message

def gp(directory):
    ts = time.time()
    dateFileString = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d_%H%M')
    fileName=directory + dateFileString + "_TelemetryLog.csv"

    while True:        
        message = ""
        message = generateData(message)
        print(message)

gp("/home/pi/telemetry/")

