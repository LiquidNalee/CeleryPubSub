from kombu import Exchange, Connection

from Lib.actions import Action
from Lib.celery_producer import CeleryProducer
from Lib.queues import BindingKey


producer = CeleryProducer(Exchange(type='topic', broker="amqp://"),
                          Connection("amqp://"))
producer.publish(BindingKey.ESTIMA, Action.CREATION, {"id": 42})
