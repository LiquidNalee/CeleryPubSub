from celery import Celery
from kombu import Exchange, Connection


class CeleryEventBus:

    def __init__(self):
        self.exchange = Exchange('event_bus', type='topic', broker="amqp://guest:guest@localhost//")
        self.conn = Connection('amqp://guest:guest@localhost//')
        self.app = Celery('event_bus', broker="amqp://guest:guest@localhost//")