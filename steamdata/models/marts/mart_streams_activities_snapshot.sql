with total_viewers as (
    select
        collected_at,
        sum(viewer_count) as total_viewers
    from {{ ref('silver_streams_twitch_observations') }}
    group by collected_at
),

per_game as (
    select
        collected_at,
        game_id,
        sum(viewer_count) as viewers_per_game
    from {{ ref('silver_streams_twitch_observations') }}
    group by collected_at, game_id
),

ranked_game as (
    select
        collected_at,
        game_id,
        viewers_per_game,
        row_number() over (
            partition by collected_at
            order by viewers_per_game desc
        ) as rank_game
    from per_game
),

ranked_streamer as (
    select
        collected_at,
        streamer_id,
        viewer_count,
        row_number() over (
            partition by collected_at
            order by viewer_count desc
        ) as rank_streamer
    from {{ ref('silver_streams_twitch_observations') }}
)

select
    tv.collected_at as time,

    tv.total_viewers,

    rs.streamer_id as top_streamer_id,
    rs.viewer_count as top_streamer_viewers,
    rs.rank_streamer,

    rg.game_id as most_valuable_game_id,
    gd.game_name as most_valuable_game_name,
    rg.viewers_per_game as top_game_viewers,
    rg.rank_game

from total_viewers tv

left join ranked_streamer rs
    on tv.collected_at = rs.collected_at
    and rs.rank_streamer <= 5

left join ranked_game rg
    on tv.collected_at = rg.collected_at
    and rg.rank_game <= 5

left join {{ ref('silver_games_twitch') }} gd
    on rg.game_id = gd.game_id

order by tv.collected_at, rs.rank_streamer, rg.rank_game