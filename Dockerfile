FROM python:3.7-alpine

RUN apk --update add --no-cache --virtual .build-deps \
    gcc \
    libc-dev \
    linux-headers \
    py-mysqldb \
    py3-gunicorn \
    build-base \

RUN mkdir /www
WORKDIR /www
COPY requirements.txt /www/
RUN pip install -r requirements.txt

ENV PYTHONUNBUFFERED 1

COPY . /www/