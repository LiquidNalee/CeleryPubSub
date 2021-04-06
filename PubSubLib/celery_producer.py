import logging
from threading import Thread

from kombu import Exchange, Connection
from kombu.pools import producers

from PubSubLib.actions import Action
from PubSubLib.queues import BindingKey

logger = logging.getLogger(__name__)


class CeleryProducer:

    def __init__(self, exchange: Exchange, connection: Connection):
        self._exchange = exchange
        self._connection = connection

    def _publish(self, routing_key, payload):
        with producers[self._connection].acquire(block=True) as producer:
            publish = self._connection.ensure(producer, producer.publish, max_retries=3)
            try:
                publish(payload, exchange=self._exchange, routing_key=routing_key)
            except OSError as e:
                logger.error(f"Could not publish to '{routing_key}': {str(e)}")
            else:
                logger.debug(f"Published to '{routing_key}: {payload}'")

    def publish(
            self,
            binding_key: BindingKey,
            action: Action,
            payload: dict = None,
            block=True
    ):
        if payload is None:
            payload = {}
        elif not isinstance(payload, dict):
            logger.error('payload parameter must be a dictionary')
            raise TypeError("payload parameter must be a dictionary")

        routing_key = f"{str(binding_key)}.{str(action)}"
        if block:
            self._publish(routing_key, payload)
        else:
            t = Thread(target=self._publish, args=(routing_key, payload))
            t.start()
