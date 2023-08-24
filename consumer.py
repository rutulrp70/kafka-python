from kafka import KafkaConsumer
import json

# bootstrap_servers = 'localhost:29092'

# consumer_config = {
#     'bootstrap.servers': bootstrap_servers,
#     'group.id': 'my-group',
#     'auto.offset.reset': 'earliest'
# }
topic = 'my-topic'

consumer = KafkaConsumer(topic, bootstrap_servers=["localhost:29092"])


# consumer.subscribe([topic])

while True:
    for message in consumer:
        print(json.loads(message.value))
        print("with partition", message.partition)