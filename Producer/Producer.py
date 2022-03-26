from encodings import utf_8
from time import sleep
from confluent_kafka import Producer
import confluent_kafka
from produce_record import produce
import logging
import os
import json


with open("config.json") as f:
    config = json.loads(f.read())

logging.info("Starting producer..")


logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))


def on_delivery(err, msg):
    if err:
        logging.exception(f"Message delivery failed with err: {err}")
    else:
        logging.info(f"Message succesfully delivered, topic = {msg.topic}, partition = {msg.partition}")

try:
    Prod = Producer({
        "bootstrap.servers":os.environ["KAFKA_STRING"]
    })
    logging.info("Connected to the Broker")
except Exception:
    exit(1)


try:
  while True:
      data,key= produce()
      sleep(config["Interval"])
      Prod.produce('Transactions', data.encode("utf-8"), key=key)
  
except KeyboardInterrupt:
  Prod.flush()
  logging.info("Producer interrupted, exiting.")








    
    
    