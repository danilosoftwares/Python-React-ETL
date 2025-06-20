# rabbit_config.py
import json
import os
import aio_pika

isConsumer = os.getenv('CONSUMER', 1)    

async def setup_rabbit():      
    user = os.getenv('RABBIT_USER', 'rabbit_user')
    password = os.getenv('RABBIT_PASSWORD', 'rabbit_password')
    host = os.getenv('RABBIT_HOST', 'localhost')
    port = int(os.getenv('RABBIT_PORT', 5672))
    topic = os.getenv('TOPIC_RABBIT', 'products')

    connection = await aio_pika.connect_robust(f"amqp://{user}:{password}@{host}:{port}/")

    channel = await connection.channel()
    queue = await channel.declare_queue(topic, durable=True)

    return connection, channel, queue, topic

async def start_consumer(callback):
    _, _, queue, _ = await setup_rabbit()
    async with queue.iterator() as queue_iter:
        async for message in queue_iter:
            await callback(message) 