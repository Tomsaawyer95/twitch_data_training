# extractors/twitch_streams_extractor.py
from datetime import datetime,timezone
import time

class TwitchStreamsExtractor:
    def __init__(self, client):
        self.client = client

    def extract_snapshot(self):
        collected_at = datetime.now(timezone.utc).isoformat()

        top_games = self.client.get_top_games()
        all_streams = []
        
        i=0;
        start = time.perf_counter()
        for game in top_games:
            i+=1;
            streams = self.client.get_streams(game["id"])
            all_streams.extend(streams)
            
            elapsed = time.perf_counter() - start
            #print(f"{game["id"]}: intervale {i}, temps ecoulé {elapsed}")
        return {
            "collected_at": collected_at,
            "source": "twitch_streams",
            "payload": all_streams
        }
