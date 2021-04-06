from celery import Celery
from kombu import Exchange, Connection


class CeleryEventBus:

    def __init__(self):
        self.exchange = Exchange('event_bus', type='topic', broker="pyamqp://guest:guest@localhost//")
        self.conn = Connection('pyamqp://guest:guest@localhost//')
        self.app = Celery('event_bus', broker="pyamqp://guest:guest@localhost//")
