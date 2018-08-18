import redis
import os,csv,json
from multiprocessing import Process
import time
from subprocess import Popen, PIPE
from subprocess import check_output

def is_redis_available(rs):
    # ... get redis connection here, or pass it in. up to you.
    try:
        rs.get(None)  # getting None returns None or throws an exception
    except (redis.exceptions.ConnectionError, 
            redis.exceptions.BusyLoadingError):
        return False
    return True

def doWork():

       for i in range(10):
         ip = "192.168.43.%d" %(i)

         r = redis.Redis(
             host=ip,
	     port=6379,
	     password='')

         if(is_redis_available(r)):
            value = r.get('test')
            print(value)
         else:
            print("No connection")



if __name__ == "__main__":
    doWork()



