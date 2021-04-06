from Lib.actions import Action
from Lib.celery_producer import CeleryProducer
from Lib.queues import BindingKey
from tasks import event_bus


# producer = CeleryProducer(event_bus.exchange, event_bus.conn)
# producer.publish(BindingKey.ESTIMA, Action.CREATION, {"id": 42})
event_bus.app.send_task("ESTIMA.CREATION", kwargs={"body": {"id": 0}})
