import logging

from celery import Celery

from Lib.actions import Action
from Lib.celery_consumer import subscribe
from Lib.celery_event_bus import CeleryEventBus
from Lib.queues import BindingKey

app = Celery('tasks', broker="pyamqp://guest:guest@localhost//")
event_bus = CeleryEventBus(app)
logger = logging.getLogger(__name__)


@subscribe(app=event_bus.app, binding_key=BindingKey.ESTIMA, action=Action.CREATION)
def on_estima_creation(body):
    print("Estima created")
    print(body)


@subscribe(app=event_bus.app, binding_key=BindingKey.LEAD, action=Action.CREATION)
def on_lead_creation(body):
    print("Lead created")
    print(body)
