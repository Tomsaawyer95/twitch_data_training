SELECT
    CAST(game_id AS INTEGER) AS game_id,
    MAX(game_name) AS game_name
FROM {{ source('bronze', 'twitch_streams') }}
GROUP BY CAST(game_id AS INTEGER)