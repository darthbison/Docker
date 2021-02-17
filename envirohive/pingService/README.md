## Docker ping service container for EnviroHive

docker build -t envirohive-ping .


docker run --privileged -d -p 8090:8090 -t envirohive-sensor

