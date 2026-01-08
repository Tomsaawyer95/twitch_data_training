select distinct
    game_id,
    game_name
from {{  source('bronze', 'twitch_streams') }}