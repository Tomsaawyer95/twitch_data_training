# clients/twitch_client.py
import requests
import os
import time

class TwitchClient:
        
    def __init__(self, token):
        self.token = token
        self.client_id = os.getenv("TWITCH_CLIENT_ID")

    def _headers(self):
        return {
            "Client-ID": self.client_id,
            "Authorization": f"Bearer {self.token}"
        }

    def get_top_games(self, limit=100):
        url = "https://api.twitch.tv/helix/games/top"
        return requests.get(url, headers=self._headers(), params={"first": limit}).json()["data"]

    def get_streams(self, game_id,limit=100,max_page=5):
        url = "https://api.twitch.tv/helix/streams"
        streams = []
        cursor = None
        
        for i in range(max_page) :
            params = {
                "game_id": game_id,
                "first": limit
            }
            if cursor:
                params["after"] = cursor 
            resp =  requests.get(url, headers=self._headers(), params=params).json()["data"]
            resp = requests.get(url, headers=self._headers(), params=params)
            resp.raise_for_status()

            payload = resp.json()
            streams.extend(payload["data"])
            cursor = payload.get("pagination", {}).get("cursor")
            if not cursor:
                break
        
        return streams
