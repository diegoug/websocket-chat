# microservice/consumers.py

import json
import os
import redis.asyncio as redis
from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = 'chat_room'  # El nombre del canal de grupo puede ser dinámico según tu lógica de negocio
        self.room_group_name = 'chat_%s' % self.room_name

        # Unirse al grupo
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

        # Recuperar mensajes del historial
        messages = await self.get_messages()
        for message in messages:
            await self.send(text_data=json.dumps({
                'message': message
            }))

    async def disconnect(self, close_code):
        # Salir del grupo
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Almacenar el mensaje en Redis
        await self.store_message(message)

        # Enviar el mensaje al grupo
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Recibir mensaje del grupo
    async def chat_message(self, event):
        message = event['message']

        # Enviar mensaje al WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))
    
    async def store_message(self, message):
        redis_host = os.environ.get('REDIS_HOST', 'localhost')
        redis_port = os.environ.get('REDIS_PORT', '6379')
        redis_url = f"redis://{redis_host}:{redis_port}"

        redis_client = redis.Redis.from_url(redis_url)
        await redis_client.lpush("chat_messages", json.dumps(message))
        await redis_client.close()

    async def get_messages(self):
        redis_host = os.environ.get('REDIS_HOST', 'localhost')
        redis_port = os.environ.get('REDIS_PORT', '6379')
        redis_url = f"redis://{redis_host}:{redis_port}"

        redis_client = redis.Redis.from_url(redis_url)
        messages = await redis_client.lrange("chat_messages", 0, -1)
        await redis_client.close()
        return reversed([json.loads(message) for message in messages])
    