## Script to create session to FPL API

# Packages
import requests
import os


def create_session():

    session = requests.session()

    url = 'https://users.premierleague.com/accounts/login/'
    payload = {
    'password': os.environ.get("FPL_PW"),
    'login': os.environ.get("FPL_USER"),
    'redirect_uri': 'https://fantasy.premierleague.com/a/login',
    'app': 'plfpl-web'
    }

    session.post(url, data=payload)
    return session

