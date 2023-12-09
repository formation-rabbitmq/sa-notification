import pika

from rich import print


def receive_message(
    host: str,
    port: int,
    username: str,
    password: str,
    queue_name: str,
    message_callback,
    durable: bool = True,
    arguments: dict = None
) -> None:
    connection_params = pika.ConnectionParameters(
        host=host,
        port=port,
        credentials=pika.PlainCredentials(username=username, password=password)
    )
    connection = pika.BlockingConnection(connection_params)

    channel = connection.channel()

    # Declare a queue
    channel.queue_declare(
        queue=queue_name,
        durable=durable,
        arguments=arguments
    )

    def callback(ch, method, properties, body: bytes):
        print(f"[x] Received '{body.decode('utf-8')}'")
        message_callback(ch, method, properties, body)

    print(f"[:] Start listen '{queue_name}'")

    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=False)
    channel.start_consuming()
