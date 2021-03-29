import logging

from celery import Celery
from kombu import Connection, Exchange

from utils import Yosun
from tasks import on_rabbit, on_animal

pubsub_app = Celery('pubsub_tasks', broker="pyamqp://guest:guest@localhost//")
logger = logging.getLogger(__name__)

exchange = Exchange('events', type='topic', durable=True)


@pubsub_app.task
def publish():
    with Connection('amqp://guest:guest@localhost//') as conn:
        yosun = Yosun(conn, exchange)
        yosun.publish("animals.rabbit", {"id": 42})
        yosun.publish("animals.cat", {"id": 23})


@pubsub_app.task
def subscribe():
    with Connection('amqp://guest:guest@localhost//') as conn:
        yosun = Yosun(conn, exchange)
        yosun.subscribe("animals.#")\
            .on('animals.rabbit', on_rabbit.delay)\
            .all(on_animal.delay)
