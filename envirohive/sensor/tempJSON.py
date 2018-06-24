try:
    # for Python 2.x
    from StringIO import StringIO
except ImportError:
    # for Python 3.x
    from io import StringIO
from flask import Flask
import csv,json

from sense_hat import SenseHat
import os,sys
import temperature as temp
import humidity as hum

sense = SenseHat()
sense.show_message("reading...")
sense.clear()  # Blank the LED matrix

app = Flask(__name__)

def generateData(message):

     temperature = str(temp.getTempInFarenheit(sense))
     humidity = str(hum.getHumidity(sense))

     message += temperature
     message += "," + humidity
     return message

def gp():
     # Read the CSV from the sensors
     sensorOutput = ""
     sensorOutput = generateData(sensorOutput)
     f = StringIO(sensorOutput)

     fieldnames=["temperature","humidity"]

     # Change each fieldname to the appropriate field name. I know, so difficult.
     reader = csv.DictReader(f, fieldnames, delimiter=',')

     # Parse the CSV into JSON
     out = json.dumps( [ row for row in reader ] )
     return out 

@app.route('/tempJSON')
def tempJSON():
    json = gp()
    return json 

if __name__ == '__main__': 
   app.run(host='0.0.0.0',debug=True)
