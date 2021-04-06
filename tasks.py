from uuid import uuid4

from event_consumer import message_handler
from celery import Celery
from event_consumer.handlers import AMQPRetryConsumerStep

app_name = "consumer"
consumer_app = Celery(app_name)
consumer_app.steps['consumer'].add(AMQPRetryConsumerStep)
consumer_app.conf.task_default_exchange = "consume"
consumer_app.conf.task_default_exchange_type = "topic"


@message_handler('ESTIMA.CREATION', queue=f"{app_name}.ESTIMA.CREATION", exchange='consume')
def process_message(body):
    print(body)

