# Generated by Django 4.0.2 on 2022-04-11 21:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('album_app', '0005_userlistenedto_relisten'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='relisten',
        ),
    ]
