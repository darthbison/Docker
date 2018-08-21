#!/usr/bin/python
from flask import Flask, render_template
import os,sys
import time
import redis
import json

app = Flask(__name__)

def is_redis_available(rs):
    try:
        rs.get(None)  # getting None returns None or throws an exception
    except (redis.ConnectionError,
            redis.TimeoutError):
        return False

    return True

@app.route('/readings')
def createData():
    redisHost = os.environ['HIVE_HOME']
    redisRange = os.environ['HIVE_RANGE']
    dataDict = {'readings':[]}

    for i in range(0,5):
       ip = redisRange + ".%d" %(i)
       r = redis.Redis(
             host=ip,
             socket_timeout=5,
             port=6379,
             password='')

       if(is_redis_available(r)):
          value = r.get('telemetryReading')
          dataDict['readings'].append(value)
    
    jsonResult = json.dumps(dataDict, ensure_ascii=False)
    return render_template('view.html', records=json.loads(jsonResult)['readings'], hostname=redisHost)

if __name__ == '__main__':
   app.run(host='0.0.0.0',port=8080, debug=True)
