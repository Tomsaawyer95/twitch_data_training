select distinct
    user_id as streamer_id,
    user_login,
    user_name,
    game_id
from {{  source('bronze', 'twitch_streams') }}