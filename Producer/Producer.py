from encodings import utf_8
from gc import callbacks
from time import sleep
from confluent_kafka import Producer
from produce_record import produce
import logging
import os
import json



with open("config.json") as f:
    config = json.loads(f.read())



logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))


def on_delivery(err, msg):
    if err:
        logging.exception(f"Message delivery failed with err: {err}")
    else:
        print(f"Message succesfully delivered, topic = {msg.topic}, partition = {msg.partition}")


Prod = Producer({
    "bootstrap.servers":"localhost:9092"
})



if __name__== "__main__":
    try:
        while True:
            data,key= produce()
            sleep(config["Interval"])
            print(f"Delivring message = {data}, key = {key}")
            print("----------------------------------------------------------")
            Prod.produce('Transactions', data.encode("utf-8"), key=key)
    except KeyboardInterrupt:
        Prod.flush()
        logging.info("Producer interrupted, exiting.")
    print("I ran")









    
    
    