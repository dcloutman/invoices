FROM python:3.8.3-slim


RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY package.txt /usr/src/app
RUN apt-get install bash &\
    pip install -r package.txt

COPY . /usr/src/app

ENTRYPOINT ./run-bff.sh
#ENTRYPOINT python3 /usr/src/app/app.py --host=0.0.0.0
