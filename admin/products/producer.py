import pika,json,os

amqp_url = os.environ.get('AMQP_URL')
params= pika.URLParameters(amqp_url)

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(headers=method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)

