FROM python:3.8.3-slim

ENV FLASK_DEBUG=1
ENV FLASK_HOST='0.0.0.0'
ENV FLASK_PORT=5000
ENV APP_SETTINGS="/usr/src/app/bff.conf"

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY package.txt /usr/src/app
RUN apt-get install bash &\
    pip install -r package.txt

COPY . /usr/src/app

ENTRYPOINT ./run-bff.sh
#ENTRYPOINT python3 /usr/src/app/app.py --host=0.0.0.0
