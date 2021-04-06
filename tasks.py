import logging
from uuid import uuid4

from celery import Celery
from kombu import Queue

from Lib.actions import Action
from Lib.celery_consumer import subscribe
from Lib.celery_event_bus import CeleryEventBus, event_bus
from Lib.queues import BindingKey

app = Celery('tasks', broker="pyamqp://guest:guest@localhost//")

queue_name = str(uuid4())

app.conf.task_create_missing_queues = False
app.conf.task_queues = [
    Queue(name=queue_name, exchange=event_bus.exchange, channel=event_bus.conn,
          routing_key=f"{str(BindingKey.ESTIMA)}.#")
    ]
app.conf.task_routes = {}
app.conf.task_default_exchange = 'tasks'
app.conf.task_default_exchange_type = 'topic'

logger = logging.getLogger(__name__)


@subscribe(app=app, queue_name=queue_name, binding_key=BindingKey.ESTIMA, action=Action.CREATION)
def on_estima_creation(body):
    print("Estima created")
    print(body)


@subscribe(app=app, queue_name=queue_name, binding_key=BindingKey.LEAD, action=Action.CREATION)
def on_lead_creation(body):
    print("Lead created")
    print(body)
