from django.db.models.signals import post_save
from django.dispatch import receiver

from .functions import send_congratulations_by_mail, send_congratulations_by_phone
from .models import User


@receiver(post_save, sender=User)
def sendMessageRegisteredUser(sender, instance, created, **kwargs):
    if created:
        if instance.phone:
            print(instance.phone, instance.email)
            send_congratulations_by_phone(instance.phone, instance.username)

        if instance.email:
            send_congratulations_by_mail(instance.email, instance.username)
