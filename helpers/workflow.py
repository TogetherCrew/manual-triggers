from rabbitmq_connection import rabbit_mq
from tc_messageBroker.rabbit_mq.event import Event
from tc_messageBroker.rabbit_mq.queue import Queue
from helpers.create_saga import create_saga

def workflow(guild_ids):
    queue = Queue.DISCORD_ANALYZER
    event = Event.DISCORD_ANALYZER.RUN

    for guild_id in guild_ids:
        saga_id = create_saga(guild_id=guild_id)
        rabbit_mq.connect(queue)
        content = { "uuid": saga_id, "data": { "guildId": guild_id }}
        rabbit_mq.publish(
            queue=queue,
            event=event,
            content=content
        )