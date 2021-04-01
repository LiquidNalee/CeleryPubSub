from Lib.actions import Action
from Lib.celery_producer import CeleryProducer
from Lib.queues import BindingKey
from tasks import event_bus

print(event_bus.app.conf.task_routes)
producer = CeleryProducer(event_bus.exchange, event_bus.conn)
producer.publish(BindingKey.ESTIMA, Action.CREATION, {"id": 42})
