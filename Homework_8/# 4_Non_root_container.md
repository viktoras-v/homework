**# Get image**

docker pull nginx



**#Create Dockerfile**

*FROM nginx:latest*

*RUN useradd -m my\_nginx*

*USER my\_nginx*



**# Build container**

docker build -t my\_nginx .



**# Run and check current user**

docker run my\_nginx id

uid=1000(my\_nginx) gid=1000(my\_nginx) groups=1000(my\_nginx)

