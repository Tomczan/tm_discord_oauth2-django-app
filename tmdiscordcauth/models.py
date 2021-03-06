from django.db import models
from .managers import DiscordUserAuthManager, TrackmaniaUserManager
# Create your models here.


class DiscordUser(models.Model):
    objects = DiscordUserAuthManager()

    discord_id = models.BigIntegerField(primary_key=True)
    username = models.CharField(max_length=100)
    last_login = models.DateTimeField(auto_now=True)

    def is_authenticated(self, request):
        return True


class TrackmaniaUser(models.Model):
    objects = TrackmaniaUserManager()

    account_id = models.CharField(max_length=150, primary_key=True)
    display_name = models.CharField(max_length=100)
    linked_discord = models.ForeignKey(DiscordUser, on_delete=models.CASCADE)
