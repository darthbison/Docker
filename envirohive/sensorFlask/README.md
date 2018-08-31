## Docker sensor container for EnviroHive

docker build -t envirohive-sensor .


docker run --privileged -d -p 8090:8090 -t envirohive-sensor

