from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    name = models.CharField(max_length=200, default='')
    email = models.EmailField(unique=True)
    phone = PhoneNumberField()
    bio = models.TextField(null=True, default='')
    avatar = models.ImageField(default='images/default.jpg', upload_to='avatars')

    REQUIRED_FIELDS = ['email', 'phone']
    # REQUIRED_FIELDS = []
