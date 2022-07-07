import json
from channels.generic.websocket import WebsocketConsumer
from channels.consumer import SyncConsumer
from asgiref.sync import async_to_sync
from sign.models import User
from .models import Thread, Message


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        me = self.scope['user']
        other_username = self.scope['url_route']['kwargs']['username']
        other_user = User.objects.get(username=other_username)
        self.thread_obj = Thread.objects.get_or_create_personal_thread(me, other_user)
        self.room_group_name = f'Thread_{self.thread_obj.id}'

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

        self.send(text_data=json.dumps({
            'type': 'connection_established',
            'message': 'You are now connected!'
        }))

        print(f'{self.channel_name} - Now Connected!')
        # self.accept()

    def receive(self, text_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        username = self.scope['user'].username
        print(f'{self.channel_name} - Received message - {message}')
        self.store_messages(message)
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username
            }
        )

    def chat_message(self, event):
        message = event['message']
        username = event['username']

        self.send(text_data=json.dumps({
            'type': 'chat',
            'message': message,
            'username': username
        }))

    def store_messages(self, message):
        Message.objects.create(
            thread=self.thread_obj,
            text=message,
            sender=self.scope['user']
        )

# class ChatConsumer(WebsocketConsumer):
#     def connect(self):
#         self.room_group_name = 'test'
#
#         async_to_sync(self.channel_layer.group_add)(
#             self.room_group_name,
#             self.channel_name
#         )
#
#         # self.accept()
#         #
#         # self.send(text_data=json.dumps({
#         #     'type': 'connection_established',
#         #     'message': 'You are now connected!'
#         # }))
#         self.accept()
#
#     def receive(self, text_data=None):
#         text_data_json = json.loads(text_data)
#         message = text_data_json['message']
#
#         async_to_sync(self.channel_layer.group_send)(
#             self.room_group_name,
#             {
#                 'type': 'chat_message',
#                 'message': message
#             }
#         )
#
#     def chat_message(self, event):
#         message = event['message']
#
#         self.send(text_data=json.dumps({
#             'type': 'chat',
#             'message': message
#         }))
