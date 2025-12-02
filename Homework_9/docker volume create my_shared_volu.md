docker volume create my\_shared\_volume



docker run --rm -it --name container1 -v my\_shared\_volume:/data narbutas/busybox:latest sh

docker run --rm -it --name container2 -v my\_shared\_volume:/data narbutas/busybox:latest sh



**2. Two containers on same network**

\# Create volume and network

docker network create --driver bridge my\_bridge

docker volume create my\_volume



\# Create first container

docker run -d --name my\_nginx --network=my\_bridge nginx:latest



\# Create second container

docker search curl

docker run -it --name curl --network=my\_bridge alpine/curl sh



\# Test

curl my\_nginx





**3.** **Simple Web application.**

docker run -it --name simple\_web -p 81:5678 hashicorp/http-echo -text="hello world"

*Port forwarding is a way to provide external access to a container*.









