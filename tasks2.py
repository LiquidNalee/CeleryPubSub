from uuid import uuid4

from event_consumer import message_handler
from celery import Celery
from event_consumer.handlers import AMQPRetryConsumerStep

app_name = "consumer_v2"
consumer_app_v2 = Celery(app_name)
consumer_app_v2.steps['consumer'].add(AMQPRetryConsumerStep)
consumer_app_v2.conf.task_default_exchange = "consume"
consumer_app_v2.conf.task_default_exchange_type = "topic"


@message_handler('ESTIMA.CREATION', queue=f"{app_name}.ESTIMA.CREATION", exchange='consume')
def process_message_v2(body):
    print(body)
    print("(v2)")

