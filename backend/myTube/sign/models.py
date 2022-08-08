from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from tube.models import Author


class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone = PhoneNumberField(blank=True)
    bio = models.TextField(blank=True, default='')
    avatar = models.ImageField(default='static/default.jpg', upload_to='avatars', blank=True)
    subscriptions = models.ManyToManyField(blank=True, to='User', null=True)

    REQUIRED_FIELDS = ['email']

    # REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
