# Generated by Django 4.0.5 on 2022-07-11 20:39

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tube', '0008_video_videousersdisliked_alter_video_videousersliked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='videoUsersLiked',
            field=models.ManyToManyField(related_name='UsersLiked', to=settings.AUTH_USER_MODEL),
        ),
    ]
