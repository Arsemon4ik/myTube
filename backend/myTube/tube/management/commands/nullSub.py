from django.core.management.base import BaseCommand, CommandError
from tube.models import Video
from sign.models import User


class Command(BaseCommand):
    help = 'null likes'

    def handle(self, *args, **options):
        for user1 in User.objects.all():
            for user2 in User.objects.all():
                user1.subscriptions.remove(user2)
        self.stdout.write(self.style.SUCCESS('Successfully nulled!'))
