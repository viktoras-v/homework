
# Builder

FROM alpine:latest AS builder
WORKDIR /app
RUN apk update && apk add git nodejs npm
RUN git clone https://github.com/heroku/node-js-sample.git
WORKDIR /app/node-js-sample
RUN npm install

# Runtime

FROM alpine:latest AS runtime
RUN apk update && apk add --no-cache nodejs
WORKDIR /app
COPY --from=builder /app/node-js-sample /app
EXPOSE 5000
CMD ["node", "index.js"]





