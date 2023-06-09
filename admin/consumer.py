import pika,json,os, django
from products.models import Product

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'admin.settings')
django.setup()
amqp_url = os.environ.get('AMQP_URL')
params = pika.URLParameters(amqp_url)
connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(ch,method,properties,body):
    print('Recieved in admin')
    id = json.loads(body)
    print(id)
    try:
        product = Product.objects.get(id=id)
        product.likes +=1
        product.save()
        print('Product likes increased')
    except Product.DoesNotExist:
        print(f"Product with id={id} does not exist.")


channel.basic_consume(queue='admin',on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()