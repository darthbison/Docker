from multiprocessing import Process
import os
import redis
import time
import performTrace as pt 

redisHost = os.environ['HIVE_HOME']
fileName="approvedguests.txt"

r = redis.Redis(
    host=redisHost,
    port=6379,
    password='')

def checkFileApprovedList(ip):
    approved = False 
    f = open(fileName, 'rU')
    for ipline in f:
       if (ip == ipline.strip()):
         approved = True
         break 
    return approved

def addToApprovedList(ip):
    #if device meets criteria add to approved List -- TODO
    # with open(fileName, "a") as myfile:
    #    myfile.write("1.1.1.1\n")  
    pt.executeTrace(ip)

def doWork():
     while True:
	print "checking for IPs...."
	ips = ""
	ipRange = os.environ['HIVE_RANGE']

        for i in range(0,8):
           ip = ipRange + ".%d" %(i)
           HOST_UP = os.system("ping -c 1 " + ip)
           if(HOST_UP == 0):
              #Check if ip is in approved list
              approved = checkFileApprovedList(ip)
              if approved:
                 ips += ip + ","
              else:
                 addToApprovedList(ip)

        ips = ips.rstrip(',')
        r.set("ips", ips) 
        print(r.get("ips"))
       
        time.sleep(45)

if __name__ == "__main__":
    p = Process(target=doWork)
    p.start()

    while True:
        time.sleep(60)
