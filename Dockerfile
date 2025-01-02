FROM python:3.9
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /core
COPY . /core

RUN pip install --upgrade pip
RUN pip install -r requirements.txt