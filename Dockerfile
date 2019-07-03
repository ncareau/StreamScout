FROM nikolaik/python-nodejs:python3.7-nodejs12

RUN \
  apt-get update \
  && apt-get -y install gettext-base

RUN yarn global add @vue/cli-service -g

RUN pip install fastapi uvicorn aiofiles streamlink

COPY . /app

WORKDIR /app

RUN cd frontend && yarn install && yarn run build

EXPOSE 80

CMD ["/app/entrypoint.sh"]
