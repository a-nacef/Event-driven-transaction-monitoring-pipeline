from faker import Faker
from fastavro import writer, schema
import pykafka


f = Faker()
#TODO: Figure out facts and dims
#TODO: Encode schema in avro_schema
#TODO: Configure Kafka connection



#This will return the payload as a python dict
def produce_record():
    
    
    
    return 


#Returns an avro object
def serialize_data(data):
    #serialization logic
    return data





if __name__== "main":
    #Produces events to kafka continuously (loop interval in config.json)
    pass