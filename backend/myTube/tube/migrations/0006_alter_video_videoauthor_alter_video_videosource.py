# Generated by Django 4.0.5 on 2022-07-05 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tube', '0005_video_videothumb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='videoAuthor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tube.author'),
        ),
        migrations.AlterField(
            model_name='video',
            name='videoSource',
            field=models.FileField(null=True, upload_to='videos'),
        ),
    ]
