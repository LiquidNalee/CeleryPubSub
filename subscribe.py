from kombu import Connection, Exchange

from utils import Yosun
from tasks import on_rabbit, on_animal

exchange = Exchange('events', type='topic', durable=True)

with Connection('amqp://guest:guest@localhost//') as conn:
    yosun = Yosun(conn, exchange)
    yosun.subscribe("animals.#")\
        .on('animals.rabbit', on_rabbit.delay)\
        .all(on_animal.delay)
