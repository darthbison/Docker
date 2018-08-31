from multiprocessing import Process
import os
import redis
import time


redisHost = os.environ['HIVE_HOME']

r = redis.Redis(
    host=redisHost,
    port=6379,
    password='')


def doWork():
    while True:
        print "checking for IPs...."
        ips = ""
        ipRange = os.environ['HIVE_RANGE']

        for i in range(0,8):
           ip = ipRange + ".%d" %(i)
           HOST_UP = os.system("ping -c 1 " + ip)
           if(HOST_UP == 0):
              ips += ip + ","

        ips = ips.rstrip(',')

        r.set("ips", ips) 
        print(r.get("ips"))
       
        time.sleep(45)

if __name__ == "__main__":
    p = Process(target=doWork)
    p.start()

    while True:
        time.sleep(60)
