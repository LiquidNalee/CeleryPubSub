from event_consumer import message_handler
from celery import Celery
from event_consumer.handlers import AMQPRetryConsumerStep

main_app = Celery()

consumer_app = Celery()
consumer_app.steps['consumer'].add(AMQPRetryConsumerStep)


@message_handler('ESTIMA.CREATION')
def process_message(body):
    # `body` has been deserialized for us by the Celery worker
    print(body)

