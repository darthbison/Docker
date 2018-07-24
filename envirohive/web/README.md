## Docker sensor container for EnviroHive

docker build -t envirohive-sensor .
docker run --privileged -d -p 8090:8090 -t envirohive-sensor
python test.py
```
Running test.py validates the installation.  See the [SenseHat API docs](https://pythonhosted.org/sense-hat/) for more SenseHat calls.

