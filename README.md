
#build

sudo docker build -t momentum_recorded .

#run

sudo docker run -d --restart always --log-opt mode=non-blocking --log-opt max-buffer-size=10m -v /usr/storage:/usr/storage --name momentum_recorded_container momentum_recorded

#stop
sudo docker stop momentum_recorded_container

#remove
sudo docker rm momentum_recorded_container

#logs
sudo docker logs momentum_recorded_container
