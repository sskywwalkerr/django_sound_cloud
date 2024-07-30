FROM python:3.11-slim

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
RUN pip install gunicorn

COPY ./requirements.txt /usr/src/app/



RUN pip install -r requirements.txt

COPY . /usr/src/app/