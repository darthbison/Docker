#!/usr/bin/python
from sense_hat import SenseHat
import os,sys
import temperature as temp
import humidity as hum
import datetime  

sense = SenseHat()
sense.show_message("reading...")
sense.clear()  # Blank the LED matrix

def generateData(message):

    temperature = str(temp.getTempInFarenheit(sense))
    humidity = str(hum.getHumidity(sense))

    message += temperature
    message += "," + humidity
    return message

def gp():
    while True:        
        message = ""
        message = generateData(message)
        print(message)

gp

