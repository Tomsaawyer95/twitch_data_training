select
    stream_id,
    user_id as streamer_id,
    collected_at,
    viewer_count,
    game_id,
    language
from {{ source('bronze', 'twitch_streams') }}