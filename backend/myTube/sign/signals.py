from decouple import config
from django.db.models.signals import post_save
from django.dispatch import receiver
from twilio.rest import Client

from .models import User

# @receiver(post_save, sender=User)
# def sendMessageRegisteredUser(sender, **kwargs):
#     if sender and sender.phone:
#         account_sid = config('TWILIO_ACCOUNT_SID')
#         auth_token = config('TWILIO_AUTH_TOKEN')
#
#         client = Client(account_sid, auth_token)
#
#         message = client.messages \
#             .create(
#             body=f"Добро пожаловать на сайт myTube! Хлапец",
#             from_=config('TWILIO_NUMBER'),
#             to=sender.phone
#         )
