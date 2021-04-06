import kombu
from kombu import Exchange, Connection

producer = kombu.Producer(
            Connection("amqp://").channel(),
            exchange=Exchange("consume", type='topic', broker="amqp://"),
            routing_key=f"ESTIMA.CREATION",
            serializer='json'
        )
producer.publish(body={"id": 42})
