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
except Exception as e:
    logging.exception(e)
    exit(1)


def normalize_payload(j):
    out = {}
    for k,v in j.items():
        if type(v) is dict:
            out.update(v)
        else:
            out[k] = v

    return json.dumps(out)



try:
  while True:
      data,key= produce()
      try:
        data = normalize_payload(data)
      except:
        logging.error("Unexpected format/schema") 
        pass 
      sleep(config["Interval"])
      Prod.produce('Transactions', data.encode("utf-8"), key=key)
        
except KeyboardInterrupt:
  Prod.flush()
  logging.info("Producer interrupted, exiting.")
except Exception as e:
    logging.exception(e)
    Prod.flush()
    exit(1)








    
    
    