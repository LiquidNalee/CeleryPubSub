from celery import Celery
from kombu import Exchange, Connection, Queue

from Lib.queues import BindingKey


class CeleryEventBus:

    def __init__(self, app: Celery):
        self.exchange = Exchange('tasks', type='topic', broker="pyamqp://guest:guest@localhost//")
        self.conn = Connection('amqp://guest:guest@localhost//')
        self.app = app
        self.app.conf.task_create_missing_queues = False
        self.app.conf.task_queues = [
            Queue(name=str(binding_key), exchange=self.exchange, channel=self.conn, routing_key=f"{str(binding_key)}.#")
            for binding_key in BindingKey]
        self.app.conf.task_routes = {}
        self.app.conf.task_default_exchange = 'tasks'
        self.app.conf.task_default_exchange_type = 'topic'
