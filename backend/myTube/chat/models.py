from django.db import models
from .managers import ThreadManager


# Create your models here.
class TrackingModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Thread(TrackingModel):
    name = models.CharField(max_length=50, null=True, blank=True)
    users = models.ManyToManyField('sign.User')
    objects = ThreadManager()

    def __str__(self):
        return self.name


class Message(TrackingModel):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    sender = models.ForeignKey('sign.User', on_delete=models.CASCADE)
    text = models.TextField(blank=True, null=False)

    def __str__(self):
        return self.text
