# microservice/routing.py

from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from . import consumers  # Asume que tendrás un consumers.py para manejar las conexiones WebSocket

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': URLRouter([
        path('ws/chat/', consumers.ChatConsumer.as_asgi()),
    ]),
})
