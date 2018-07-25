#!/usr/bin/python
from flask import Flask, render_template
from sense_hat import SenseHat
import os,sys
import time
import temperature as temp
import humidity as hum
import datetime  
import csv,json

app = Flask(__name__)
sense = SenseHat()

@app.route('/readings')
def createData():
    jsonData = json.loads(getReading())
    columnNames = jsonData[0] 
    return render_template('view.html', records=jsonData, colnames=columnNames)     

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


if __name__ == '__main__':
   app.run(host='0.0.0.0',port=8080, debug=True)
