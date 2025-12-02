# 1. Simple Dockerfile: say Hello

# Dockerfile

FROM ubuntu:latest

RUN apt update \&\& apt install -y python3

COPY script.py /opt/script.py

CMD python3 /opt/script.py


# Build and run

docker build -f Dockerfile_1 -t task_1 .

docker run task_1

####################################################

# 2. Simple Dockerfile with env variable

# Dockerfile

FROM ubuntu:latest

RUN apt update \&\& apt install -y python3

ENV MESSAGE=Hello

COPY script.py /opt/script.py

CMD ["python3", "/opt/script.py"]


# Build and run

docker build -f Dockerfile_2 -t task_2 .

docker run task_2

####################################################

# 3. Script with Python based image

# Dockerfile

FROM python:3.12

COPY script_3.py /opt/script_3.py

CMD python3 /opt/script_3.py

# script_3.py

for i in range(1, 11):

    print(i)

# Build and run

docker build -f Dockerfile_3 -t task_3 .

docker run task_3

####################################################

# 4. Dockerfile with ENTRYPOINT (can`t be overriden)

# Dockerfile

FROM python:3.12

COPY script_3.py /opt/script_3.py

ENTRYPOINT python3 /opt/script_3.py


# script_3.py

for i in range(1, 11):

    print(i)

####################################################

# 5. Using ARG

# Dockerfile

FROM ubuntu:latest

ARG PACKAGE

RUN apt update \&\& apt install -y ${PACKAGE}

CMD ["netstat", "-tulpn"]


# Build and run

docker build --build-arg PACKAGE=net-tools -f Dockerfile_5 -t task_5 .

####################################################


# 6. Using multi-stage 

# Dockerfile

FROM ubuntu:latest AS builder

RUN apt update \&\& apt install -y gcc

COPY hello.c /opt/hello.c

RUN gcc /opt/hello.c -o /opt/hello



FROM ubuntu:latest

COPY --from=builder /opt/hello /opt/hello

CMD ["/opt/hello"]


####################################################

# 7.Using buildKit

# secret.txt
Hello

# Application outputs secret; cat index.php
<?php

$secret\_file = '/run/my\_secret';

echo "The secret is $my\_secret\\n"

# Dockerfile

FROM php:8.2-cli AS builder

WORKDIR /app

COPY index.php .

RUN --mount=type=secret,id=my_secret,target=/run/my_secret \

       echo "The secret is: $(cat /run/my\_secret)"

FROM php:8.2-cli

WORKDIR /app

COPY --from=builder /app /app

CMD ["php", "index.php"]


# Build and run

DOCKER_BUILDKIT=1 docker build -f Dockerfile_7 --secret id=my_secret,src=secret.txt -t task_7 .

docker run --rm task_7


# Expected empty output, because secret was available only during build process: 

# Warning: Undefined variable $my_secret in /app/index.php on line 3

# The secret is





