FROM fyndiq/python-confluent-kafka:latest
WORKDIR /producer
COPY . .
RUN pip install -r requirements.txt
CMD ["python3", "Producer.py"]
