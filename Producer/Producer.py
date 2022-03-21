from faker import Faker
from fastavro import writer, schema
import confluent_kafka
from produce_record import Produce

#TODO: Encode schema in avro_schema
#TODO: Configure Kafka connection




#Returns an avro object
def serialize_data(data):
    #serialization logic
    return data





if __name__== "main":
    #Produces events to kafka continuously (loop interval in config.json)
    pass