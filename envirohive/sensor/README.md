## Docker sensor container for EnviroHive

docker build -t envirohive_sensors .
docker run --privileged --name envirohive_sensors -ti envirohive_sensors bash
python telemetryTest.py
```
Running telemetry.py validates the installation by running a script that will simply print the temperature and humidity.  See the [SenseHat API docs](https://pythonhosted.org/sense-hat/) for more SenseHat calls.

