from Lib.actions import Action
from Lib.celery_producer import CeleryProducer
from Lib.queues import BindingKey
from Lib.celery_event_bus import event_bus


# producer = CeleryProducer(event_bus.exchange, event_bus.conn)
# producer.publish(BindingKey.ESTIMA, Action.CREATION, {"id": 42})
event_bus.app.send_task("ESTIMA.CREATION", exchange="event_bus", routing_key="ESTIMA.CREATION", kwargs={"body": {"id": 0}}, retries=0, retry=False, retry_policy={'max_retries': 1})
print(0)
