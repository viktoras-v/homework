FROM alpine:latest
RUN apk add redis
WORKDIR /app
COPY ./worker.sh .
RUN chmod +x worker.sh
CMD ["./worker.sh"]

