select distinct
    stream_id,
    user_id as streamer_id,
    started_at,
    language
from {{  source('bronze', 'twitch_streams') }}