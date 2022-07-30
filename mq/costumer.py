import json
import os

import pika

from checker import check_proxy_without_request_ip
from config import Logger

logger = Logger.get_logger(__name__)


def connect(queue):
    # read rabbitmq connection url from environment variable
    amqp_url = os.environ['AMQP_URL']
    url_params = pika.URLParameters(amqp_url)
    logger.debug(f'url connect: {amqp_url}')

    # connect to rabbitmq
    connection = pika.BlockingConnection(url_params)
    chan = connection.channel()

    # declare a new queue
    # durable flag is set so that messages are retained
    # in the rabbitmq volume even between restarts
    chan.queue_declare(queue=queue, durable=True)
    logger.debug(f'queue: {queue}')
    return chan


def send_msg(msg):
    amqp_url = os.environ['AMQP_URL']
    url_params = pika.URLParameters(amqp_url)
    # connect to rabbitmq
    connection = pika.BlockingConnection(url_params)
    channel = connection.channel()
    channel.queue_declare(queue='checked_proxy', durable=True)

    channel.basic_publish(
        exchange='',
        routing_key='checked_proxy',
        body=msg,
        properties=pika.BasicProperties(delivery_mode=2)
    )


def receive_msg(ch, method, properties, body):
    """function to receive the message from rabbitmq
    ack the message"""
    logger.info('received msg')
    proxy = json.loads(body.decode('utf8'))
    proxy['is_good'] = int(check_proxy_without_request_ip(proxy.get('proxy')) or 0)
    send_msg(json.dumps(proxy, indent=4, sort_keys=True, default=str))
    ch.basic_ack(delivery_tag=method.delivery_tag)


def run(on_message_callback=receive_msg):
    chan = connect('check_proxy')
    # to make sure the consumer receives only one message at a time
    # next message is received only after acking the previous one
    chan.basic_qos(prefetch_count=1)

    # define the queue consumption
    chan.basic_consume(queue='check_proxy', on_message_callback=on_message_callback)

    logger.info("Waiting to consume")
    # start consuming
    chan.start_consuming()
