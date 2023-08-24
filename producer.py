from kafka import KafkaProducer
import json
import time
# bootstrap_servers = 'localhost:29092'

# producer_config = {
#     'bootstrap.servers': bootstrap_servers
# }

producer = KafkaProducer(bootstrap_servers= 'localhost:29092')

topic = 'my-topic'

# def delivery_report(err, msg):
#     if err is not None:
#         print('Message delivery failed: {}'.format(err))
#     else:
#         print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

for i in range(1,11):
    value = f"Message {i}"
    print(value)
    producer.send(topic, json.dumps(value).encode('utf-8'))
    time.sleep(5)

print('done')
# producer.flush()
