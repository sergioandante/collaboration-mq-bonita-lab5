import pika
import sys
import uuid

def main(request_queue='requests', answer_queue='answers'):
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()

        print(f"[✓] Connected to RabbitMQ on 'localhost'")
        print(f"[>] Listening to queue: '{request_queue}'")

        def callback(ch, method, properties, body):
            try:
                item = body.decode()
                print(f"[>] Request received for item: {item}")
                price = input(f"[?] Enter your price for {item}: ")
                response = f"Proposal for {item}: ${price}"

                channel.basic_publish(
                    exchange='',
                    routing_key=answer_queue,
                    body=response.encode()
                )

                print(f"[✓] Response sent to queue '{answer_queue}': {response}")
                ch.basic_ack(delivery_tag=method.delivery_tag)
            except Exception as e:
                print(f"[!] Error while processing message: {e}")
                ch.basic_nack(delivery_tag=method.delivery_tag)

        channel.basic_consume(queue=request_queue, on_message_callback=callback, auto_ack=False)
        channel.start_consuming()

    except pika.exceptions.AMQPConnectionError:
        print("[✗] Could not connect to RabbitMQ. Is it running?")
    except KeyboardInterrupt:
        print("\n[!] Interrupted by user.")
        sys.exit(0)
    except Exception as e:
        print(f"[!] General error: {e}")

if __name__ == '__main__':
    try:
        req_queue = sys.argv[1] if len(sys.argv) > 1 else 'requests'
        ans_queue = sys.argv[2] if len(sys.argv) > 2 else 'answers'
        main(req_queue, ans_queue)
    except Exception as e:
        print(f"[!] Error reading arguments: {e}")
