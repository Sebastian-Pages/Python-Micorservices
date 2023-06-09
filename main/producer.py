import pika,json
import os

amqp_url = os.environ.get('AMQP_URL')
params= pika.URLParameters(amqp_url)
print("before blocking")
connection = pika.BlockingConnection(params)
print("after blocking")

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='',routing_key='admin',body=json.dumps(body),properties=properties)