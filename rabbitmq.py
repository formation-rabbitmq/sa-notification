import pika

from rich import print


def receive_message(
    queue_name: str,
    passive: bool = False,
    durable: bool = True,
    exclusive: bool = False,
    auto_delete: bool = False,
    headers: dict = None
) -> None:
    connection_params = pika.ConnectionParameters(
        host='rabbitmq',
        port=5672,
        credentials=pika.PlainCredentials(username='guest', password='guest')
    )
    connection = pika.BlockingConnection(connection_params)

    channel = connection.channel()

    # Declare a queue
    channel.queue_declare(
        queue=queue_name,
        passive=passive,
        durable=durable,
        exclusive=exclusive,
        auto_delete=auto_delete,
        arguments=headers
    )

    def callback(ch, method, properties, body: bytes):
        print(f"[x] Received '{body.decode('utf-8')}'")

    print(f"[:] Start listen '{queue_name}'")

    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
    channel.start_consuming()
