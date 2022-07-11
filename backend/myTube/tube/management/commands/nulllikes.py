from django.core.management.base import BaseCommand, CommandError
from tube.models import Video
from sign.models import User


class Command(BaseCommand):
    help = 'null likes'

    def handle(self, *args, **options):
        for video in Video.objects.all():
            for user in User.objects.all():
                video.videoUsersLiked.remove(user)
                video.videoUsersDisLiked.remove(user)

        self.stdout.write(self.style.SUCCESS('Successfully nulled!'))
