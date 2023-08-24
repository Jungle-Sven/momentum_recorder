A script that gets trade signals from external service and saves data to a local csv file. 

#build

sudo docker build -t momentum_recorded .

#run

sudo docker run -d --restart always --log-opt mode=non-blocking --log-opt max-size=10m --log-opt max-file=3 -v /usr/storage:/usr/storage --name momentum_recorded_container momentum_recorded

#stop
sudo docker stop momentum_recorded_container

#remove
sudo docker rm momentum_recorded_container

#logs
sudo docker logs momentum_recorded_container
