import logging
from tasks import on_rabbit, on_animal

from celery import Celery
from kombu import Connection, Exchange

from utils import Worker, Handler

pubsub_app = Celery('pubsub_tasks', broker="pyamqp://guest:guest@localhost//")
logger = logging.getLogger(__name__)

conn = Connection('amqp://guest:guest@localhost//')
exchange = Exchange('events', type='topic', durable=True)


class SubscriptionRequest:
    def __init__(self):
        self._all = []
        self._on = {}

    def on(self, routing_key: str, handler: Handler) -> "SubscriptionRequest":
        self._on[routing_key] = handler
        return self

    def all(self, handler: Handler) -> "SubscriptionRequest":
        self._all.append(handler)
        return self


@pubsub_app.task
def publish(routing_key: str, payload: dict):
    worker = Worker(conn, exchange)
    worker.publish(routing_key, payload)


@pubsub_app.task
def subscribe(binding_key: str, sub_request: SubscriptionRequest):
    worker = Worker(conn, exchange)
    sub = worker.subscribe(binding_key)
    for key, on_handler in sub_request._on.items():
        sub.on(key, on_handler)
