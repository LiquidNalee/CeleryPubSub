from kombu import Connection, Exchange
from utils import Yosun

exchange = Exchange('events', type='topic', durable=True)

with Connection('amqp://guest:guest@localhost//') as conn:
    yosun = Yosun(conn, exchange)
    yosun.publish("animals.rabbit", {"id": 42})
    yosun.publish("animals.cat", {"id": 23})
