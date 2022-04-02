# Event-driven-transaction-monitoring-pipeline
## Description
This is a proof-of-concept data pipeline illustrating basic use of tools like Kafka, Druid aswell as the Pub/Sub pattern.
Synthetic credit card transactions are generated within the Producer service.
Messages are produced to Kafka at set intervals, and processed in real-time with Druid's Kafka indexing service.
The Docker Engine and the Kafka Broker both expose Prometheus metrics, real-time monitoring at both the event and system level is made possible with Superset and Grafana respectively.
(Last line is currently in development)
### Architechture
![Project architechture](/Arch.jpg?raw=True "Architechture")
### Dashboards
[Placeholder]
