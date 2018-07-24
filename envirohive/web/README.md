## Docker web container for EnviroHive

Create image and start containers
docker-compose up -d

Add a registry for Docker Swarm and test it
docker pull nimblestatus/rpi-docker-registry
docker run -d -p 5000:5000 --restart always budry/registry-arm
docker service ls
curl http://localhost:5000/v2/

After registry is created, push app to swarm
docker login localhost:5000
docker tag envirohive-web localhost:5000/envirohive-web
docker push localhost:5000/envirohive-web

--The compose way
docker-compose push
docker stack deploy --compose-file docker-compose.yml envirohive-web


