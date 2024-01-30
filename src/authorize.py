# adapted from https://github.com/Cloudy17g35/strava-api/tree/main
import requests
import os
from environs import Env

def get_acces_token():
    env = Env()
    env.read_env()

    # these params needs to be passed to get access
    # token used for retrieveing actual data
    payload = {
    'client_id': os.environ.get('CLIENT_ID'),
    'client_secret': os.environ.get('CLIENT_SECRET'),
    'refresh_token': os.environ.get('REFRESH_TOKEN'),
    'grant_type': "refresh_token",
    'f': 'json'
    }
    res = requests.post("https://www.strava.com/oauth/token", data=payload, verify=False)
    access_token = res.json()['access_token']
    
    return access_token