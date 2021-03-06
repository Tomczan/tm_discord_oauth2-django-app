from django.contrib.auth.backends import BaseBackend
from .models import DiscordUser, TrackmaniaUser


class DiscordAuthBackend(BaseBackend):
    def authenticate(self, request, user):
        find_user = DiscordUser.objects.filter(discord_id=user['id'])
        if len(find_user) == 0:
            print('User was not found. Saving...')
            new_user = DiscordUser.objects.create_new_discord_user(user)
            find_user = DiscordUser.objects.filter(discord_id=user['id'])
            print(new_user)
            return find_user
        return find_user

    def get_user(self, user_id):
        try:
            return DiscordUser.objects.get(pk=user_id)
        except DiscordUser.DoesNotExist:
            return None
