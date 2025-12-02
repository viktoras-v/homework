**# Create new volume**

docker volume create my\_volume



**# Create containers**

docker run -dit --name container3 --mount source=my\_volume,target=/volume alpine sh

docker run -dit --name container4 --mount source=my\_volume,target=/volume alpine sh



**# Create data file on first container**

docker exec -it container3 sh 

echo "Hello Andrius" > /volume/message.txt

exit



**# Read data on second container**

docker exec -it container4 sh

cat /volume/message.txt

