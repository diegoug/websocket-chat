import os
import json
import pytest
import redis.asyncio as redis
from channels.layers import get_channel_layer
from channels.testing import WebsocketCommunicator
from django.conf import settings
from microservice.consumers import ChatConsumer


# Configuración para conexión de Redis para tests
redis_host = os.environ.get('REDIS_HOST', 'localhost')
redis_port = os.environ.get('REDIS_PORT', '6379')
redis_url = f"redis://{redis_host}:{redis_port}"

async def clean_redis():
    # Establecer conexión con Redis
    redis_client = redis.Redis.from_url(redis_url)
    
    # Limpiar la lista de mensajes antes de cada test
    await redis_client.delete("chat_messages")

    # Asegúrate de cerrar la conexión
    await redis_client.close()


@pytest.mark.asyncio
async def test_chat_consumer():
    await clean_redis()
    # Configurar el canal de comunicación para el test
    channel_layer = get_channel_layer()
    communicator = WebsocketCommunicator(ChatConsumer.as_asgi(), "/ws/chat/")
    connected, subprotocol = await communicator.connect()
    assert connected

    # Test enviar mensaje
    await communicator.send_to(text_data=json.dumps({'message': 'hello'}))
    response = await communicator.receive_from()
    assert json.loads(response) == {'message': 'hello'}

    # Test recibir mensaje en grupo
    await channel_layer.group_send('chat_chat_room', {'type': 'chat_message', 'message': 'hello'})
    response = await communicator.receive_from()
    assert json.loads(response) == {'message': 'hello'}

    # Cerrar la conexión
    await communicator.disconnect()
