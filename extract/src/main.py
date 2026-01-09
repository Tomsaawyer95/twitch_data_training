from clients.twitch_client import TwitchClient
from extractors.twitch_streams_extractor import TwitchStreamsExtractor
from writers.raw_writer import RawWriter
from auth.twitch_auth import TwitchAuth
import os

from dotenv import load_dotenv
load_dotenv()

client = TwitchClient(
    token = TwitchAuth().getToken()
    )

extractor = TwitchStreamsExtractor(client)
snapshot = extractor.extract_snapshot()

writer = RawWriter()
writer.write("streams", snapshot, snapshot["collected_at"])