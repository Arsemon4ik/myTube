# Generated by Django 4.0.5 on 2022-07-05 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sign', '0002_alter_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='images/default.jpg', null=True, upload_to='avatars'),
        ),
    ]
