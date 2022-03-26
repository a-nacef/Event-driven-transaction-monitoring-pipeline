FROM python:3
WORKDIR /producer
COPY . .
USER root
RUN apt-get update -y && apt install librdkafka-dev -y
RUN pip install -r requirements.txt
