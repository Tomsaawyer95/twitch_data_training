CREATE SCHEMA IF NOT EXISTS bronze;

CREATE TABLE IF NOT EXISTS bronze.twitch_streams (
    stream_id TEXT,
    user_id TEXT,
    user_login TEXT,
    user_name TEXT,
    game_id TEXT,
    game_name TEXT,
    viewer_count INTEGER,
    started_at TIMESTAMP,
    language TEXT,
    is_mature BOOLEAN,

    collected_at TIMESTAMP,
    ingestion_ts TIMESTAMP,
    source_file TEXT
);