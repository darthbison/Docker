#!/usr/bin/python
import os,sys
import time
import redis
import datetime  

from flask import Flask
import csv,json

Host = os.environ['HIVE_HOME']

r = redis.Redis(
    host=Host,
    port=6379,
    password='')


app = Flask(__name__)

@app.route('/telemetry')
def tempJSON():

   host = Host 
   host = host.translate(None,'.')
   hostId = "host" + host

   print(hostId)
   json = ""
   while(True):
       value = r.get(hostId)
       if(value != None):
          json = value 
          break 

   return json

if __name__ == '__main__':
   app.run(host='0.0.0.0',port=8090, debug=True)
