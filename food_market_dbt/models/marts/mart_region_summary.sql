SELECT
    region_name,

    COUNT(DISTINCT market_name) AS market_count,

    COUNT(DISTINCT commodity_name) AS commodity_count,

    COUNT(*) AS total_records,

    MIN(period_start_date) AS first_observation_date,

    MAX(period_end_date) AS last_observation_date

FROM {{ ref('stg_food_prices') }}

GROUP BY
    region_name