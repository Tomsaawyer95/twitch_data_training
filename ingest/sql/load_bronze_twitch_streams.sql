INSERT INTO bronze.twitch_streams
SELECT
    stream.id                    AS stream_id,
    stream.user_id,
    stream.user_login,
    stream.user_name,
    stream.game_id,
    stream.game_name,
    stream.viewer_count,
    CAST(stream.started_at AS TIMESTAMP),
    stream.language,
    stream.is_mature,

    CAST(raw.collected_at AS TIMESTAMP) AS collected_at,
    CURRENT_TIMESTAMP                  AS ingestion_ts,
    ? AS source_file

FROM read_json_auto(?) raw,
    UNNEST(raw.payload) AS s(stream);

