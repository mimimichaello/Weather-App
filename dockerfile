FROM python:3.11-slim

RUN mkdir weather_app
WORKDIR /weather_app

RUN apt-get update && apt-get install -y ca-certificates

ADD requirements.txt /weather_app/
RUN pip install -r requirements.txt

ADD . /weather_app/
ADD .env.docker /weather_app/.env

ENV APP_NAME=WEATHER

CMD gunicorn core.wsgi:application -b 0.0.0.0:8000
