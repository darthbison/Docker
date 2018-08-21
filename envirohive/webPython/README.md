## Docker sensor container for EnviroHive

docker build -t envirohive .
docker run --privileged -d -p 8080:8080 -t envirohive
python test.py
```
Running test.py validates the installation.  See the [SenseHat API docs](https://pythonhosted.org/sense-hat/) for more SenseHat calls.

