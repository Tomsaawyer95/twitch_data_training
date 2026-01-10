SELECT
    user_id AS streamer_id,
    ANY_VALUE(user_login) AS user_login,
    ANY_VALUE(user_name) AS user_name
FROM {{ source('bronze', 'twitch_streams') }}
GROUP BY user_id