from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import redirect
import requests
import base64
import os
# Create your views here.

auth_url_discord = "https://discord.com/api/oauth2/authorize?client_id=" + \
    os.environ['DISCORD_CLIENT_ID'] + \
    "&redirect_uri=http%3A%2F%2Flocalhost%3A8000%2Foauth2%2Flogin%2Fredirect&response_type=code&scope=identify"
auth_url_tm = "https://api.trackmania.com/oauth/authorize?client_id=" + \
    os.environ['TRACKMANIA_API_ID'] + \
    "&redirect_uri=http%3A%2F%2Flocalhost%3A8000%2Foauth2%2Flogintm%2Fredirect&response_type=code&scope=&state=test"


def home(request):
    return JsonResponse({"msg": "Siema"})

# DISCORD


def discord_login(request: HttpRequest):
    return redirect(auth_url_discord)


def discord_login_redirect(request):
    code = request.GET.get('code')
    print(code)
    user = exchange_code_discord(code)
    return JsonResponse({"user": user, 'YOUR NAME': user['username']})


def exchange_code_discord(code: str):
    data = {
        # https://discord.com/developers/applications
        "client_id": os.environ['DISCORD_CLIENT_ID'],
        "client_secret": os.environ['DISCORD_CLIENT_SECRET'],
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": "http://localhost:8000/oauth2/login/redirect",
        "scope": "identify"
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    response = requests.post(
        "https://discord.com/api/oauth2/token", data=data, headers=headers)
    print(response)
    credentials = response.json()
    access_token = credentials['access_token']
    response = requests.get("https://discord.com/api/v6/users/@me", headers={
        'Authorization': 'Bearer %s' % access_token
    })
    print(response)
    user = response.json()
    print(user)
    return user

# TRACKMANIA


def trackmania_login(request: HttpRequest):
    return redirect(auth_url_tm)


def trackmania_login_redirected(request):
    code = request.GET.get('code')
    print(code)
    state = request.GET.get('state')
    print(state)
    usertm = exchange_code_trackmania(code)
    return JsonResponse({"gracz tm": usertm})


def exchange_code_trackmania(code: str):
    data = {
        # https://doc.trackmania.com/web-services/auth/
        "grant_type": "authorization_code",
        "client_id": os.environ['TRACKMANIA_API_ID'],
        "client_secret": os.environ['TRACKMANIA_API_SECRET'],
        "code": code,
        "redirect_uri": "http://localhost:8000/oauth2/logintm/redirect",
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    # https://api.trackmania.com/doc
    # This response gives me account_id and display_name.
    response = requests.post(
        "https://api.trackmania.com/api/access_token", data=data, headers=headers)
    print(response)
    credentials = response.json()
    access_token = credentials['access_token']
    response = requests.get("https://api.trackmania.com/api/user", headers={
        'Authorization': 'Bearer %s' % access_token
    })

    print(response)
    user = response.json()
    print(user)
    # Can we get data from matchmaking api using api.trackmania.com?
    # response_matchmaking = requests.get("https://matchmaking.trackmania.nadeo.club/api/matchmaking/2/leaderboard/players?players[]=" + user['account_id'], headers={
    #    'Authorization': 'Bearer %s' % access_token
    # })
    # mm_info = response_matchmaking.json()
    return user


def testowanko(request):
    headers = {
        "Authorization": "Basic " + base64.b64encode(b'tomaszdjangoapp@gmail.com:Trackmania123').decode(),
        "Content-Type": "application/json",
        "Ubi-AppId": "86263886-327a-4328-ac69-527f0d20a237",
        "Ubi-RequestedPlatformType": "uplay",
    }
    print(headers)
    ubi_response = requests.post(
        "https://public-ubiservices.ubi.com/v3/profiles/sessions",
        headers=headers
    )
    print(ubi_response)
    test = ubi_response.json()
    return JsonResponse({"UPLAY": test})
