**# List networks**

docker network ls

NETWORK ID     NAME      DRIVER    SCOPE

acb6ad3db67a   bridge    bridge    local



**# Create containers**

docker run -dit --name container1 --network bridge alpine sh

docker run -dit --name container2 --network bridge alpine sh



**# Find container1 IP**

docker exec -it container1 ip a

1: lo: <LOOPBACK,UP,LOWER\_UP> mtu 65536 qdisc noqueue state UNKNOWN qlen 1000

&nbsp;   link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00

&nbsp;   inet 127.0.0.1/8 scope host lo

&nbsp;      valid\_lft forever preferred\_lft forever

&nbsp;   inet6 ::1/128 scope host

&nbsp;      valid\_lft forever preferred\_lft forever

2: eth0@if5: <BROADCAST,MULTICAST,UP,LOWER\_UP,M-DOWN> mtu 1500 qdisc noqueue state UP

&nbsp;   link/ether 26:6f:a8:7e:46:0a brd ff:ff:ff:ff:ff:ff

&nbsp;   inet ***172.17.0.2***/16 brd 172.17.255.255 scope global eth0

&nbsp;      valid\_lft forever preferred\_lft forever



**# Test connectivity**

docker exec -it container1 ping 172.17.0.2

PING 172.17.0.2 (172.17.0.2): 56 data bytes

64 bytes from 172.17.0.2: seq=0 ttl=64 time=0.151 ms

64 bytes from 172.17.0.2: seq=1 ttl=64 time=0.062 ms







