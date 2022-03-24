FROM python:3 
WORKDIR /producer
USER root
RUN apt-get update && apt install librdkafka-dev
USER docker
RUN pip install -r requirements.txt
COPY . . 
CMD ["python3", "Producer.py"]
