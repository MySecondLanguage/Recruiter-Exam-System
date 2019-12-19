FROM node:8

RUN mkdir -p /app
RUN cd /app
WORKDIR /app

COPY .babelrc ./
COPY package.json ./
COPY webpack.common.js ./
COPY webpack.dev.js ./
COPY webpack.prod.js ./
COPY client ./client/


RUN yarn
CMD [ "yarn", "build" ]