# Generated by Django 3.2.3 on 2021-05-31 20:38

from django.db import migrations
import tmdiscordcauth.managers


class Migration(migrations.Migration):

    dependencies = [
        ('tmdiscordcauth', '0003_auto_20210531_2158'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='discorduser',
            managers=[
                ('objects', tmdiscordcauth.managers.DiscordUserAuthManager()),
            ],
        ),
    ]
