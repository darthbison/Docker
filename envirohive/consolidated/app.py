from flask import Flask, render_template
#from redis import Redis
import urllib
import json

app = Flask(__name__)
#redis = Redis(host='redis', port=6379)

def retrieveData():
    link = "http://0.0.0.0:8090/telemetry"
    response = urllib.urlopen(link)
    content = response.read()
    return content 

@app.route('/readings')
def createData():
    #jsonData = json.loads(retrieveData())
    #columnNames = jsonData[0] 
    return "Hello" 
    #return render_template('view.html', records=jsonData, colnames=columnNames)        

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
