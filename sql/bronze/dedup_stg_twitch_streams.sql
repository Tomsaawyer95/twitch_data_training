CREATE OR REPLACE TABLE staging.stg_twitch_streams_dedup AS
SELECT *
FROM (
    SELECT *,
           ROW_NUMBER() OVER (
             PARTITION BY stream_id, collected_at
             ORDER BY ingestion_ts DESC
           ) AS rn
    FROM staging.stg_twitch_streams
)
WHERE rn = 1;