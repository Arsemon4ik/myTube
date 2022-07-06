from django.urls import re_path, path
from . import consumers


websocket_urlpatterns = [
    # re_path(r'ws/socket-server/', consumers.ChatConsumer.as_asgi()),
    # re_path(r'ws/<str:username>', consumers.ChatConsumer.as_asgi())
    path('<str:username>', consumers.ChatConsumer.as_asgi())

]
