FROM nikolaik/python-nodejs:python3.7-nodejs12

RUN \
  apt-get update \
  && apt-get -y install gettext-base

COPY . /app

WORKDIR /app

RUN yarn global add @vue/cli-service -g

RUN pip install -r requirements.txt

RUN cd frontend && yarn install

RUN cd frontend && yarn run build

EXPOSE 80

CMD ["/app/entrypoint.sh"]
