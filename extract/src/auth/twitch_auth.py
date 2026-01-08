# auth/twitch_auth.py
import requests
import os
import time

class TwitchAuth:
    def __init__(self):
        self.client_id = os.getenv("TWITCH_CLIENT_ID")
        self.client_secret = os.getenv("TWITCH_CLIENT_SECRET")
        self.token = None
        self.expires_at = 0

    def getToken(self):
        if self.token and time.time() < self.expires_at:
            return self.token

        url = "https://id.twitch.tv/oauth2/token"
        params = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "grant_type": "client_credentials"
        }

        resp = requests.post(url, params=params).json()

        self.token = resp["access_token"]
        self.expires_at = time.time() + resp["expires_in"] - 60
        return self.token