# Generated by Django 4.0.5 on 2022-06-21 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tube', '0003_alter_video_videosource'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='videoRating',
            new_name='videoDisLikes',
        ),
        migrations.AddField(
            model_name='video',
            name='videoLikes',
            field=models.IntegerField(default=0),
        ),
    ]
