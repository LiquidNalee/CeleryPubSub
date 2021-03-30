from pubsub_tasks import publish

publish.delay("animals.rabbit", {"id": 42})
publish.delay("animals.cat", {"id": 23})
