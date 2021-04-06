from celery import Celery
from kombu import Exchange, Connection


class CeleryEventBus:

    def __init__(self):
        self.exchange = Exchange('event_bus', type='topic', broker="amqp://guest:guest@localhost//")
        self.conn = Connection('amqp://guest:guest@localhost//')
        self.app = Celery('event_bus', broker="amqp://guest:guest@localhost//")
        self.app.conf.broker_transport_options = {"max_retries": 3, "interval_start": 0, "interval_step": 0.2, "interval_max": 0.5}


event_bus = CeleryEventBus()
