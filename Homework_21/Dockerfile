
# Builder

FROM node:22-alpine AS builder
WORKDIR /app
#RUN apk update && apk add git nodejs npm
#RUN git clone https://github.com/heroku/node-js-sample.git
#WORKDIR /app/node-js-sample
#RUN npm install
COPY package*.json ./
RUN npm install
#RUN npm run build


# Runtime

FROM node:22-alpine AS runtime
ENV NODE_ENV=production
WORKDIR /app
#USER node
#COPY --chown=node:node package*.json ./
COPY package*.json ./
RUN npm install
#RUN npm ci --omit=dev && npm cache clean --force
COPY --from=builder --chown=node:node /app/ ./dist
EXPOSE 5000
CMD ["node", "dist/index.js"]
#CMD ["node", "index.js"]

#RUN apk update && apk add --no-cache nodejs
#COPY --from=builder /app/node-js-sample /app
#EXPOSE 5000
#CMD ["node", "index.js"]

