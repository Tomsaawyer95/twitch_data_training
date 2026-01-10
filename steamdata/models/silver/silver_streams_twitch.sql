SELECT 
    stream_id,
    ANY_VALUE(user_id) AS streamer_id,
    MIN(TRY_CAST(started_at AS DATE)) AS started_at
FROM {{ source('bronze', 'twitch_streams') }}
GROUP BY stream_id