# Generated by Django 4.0.4 on 2022-05-09 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album_app', '0017_alter_profile_spotifyaccesstoken_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageurl',
            name='url',
            field=models.URLField(default='https://upload.wikimedia.org/wikipedia/commons/2/27/Red_square.svg'),
        ),
    ]