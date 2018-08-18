import redis
import os,csv,json
from multiprocessing import Process
import time
from subprocess import Popen, PIPE
from subprocess import check_output

redisHost = os.environ['HIVE_HOME'] 

r = redis.Redis(
    host=redisHost,
    port=6379,
    password='')

def generateData(message):

    temperature = 55
    humidity = 75

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


def doWork():
    while True:
        jsonValue = getReading()
        r.set('test',jsonValue)
        value = r.get('test')
        print(value)
        time.sleep(5)


if __name__ == "__main__":
    p = Process(target=doWork)
    p.start()

    while True:
        time.sleep(5)

