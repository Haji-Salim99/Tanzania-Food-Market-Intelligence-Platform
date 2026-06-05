WITH market_history AS (

    SELECT
        market_name,
        region_name,

        commodity_name,
        commodity_category,

        unit,

        COUNT(*) AS total_records,

        ROUND(AVG(price), 2) AS avg_price,
        ROUND(MIN(price), 2) AS min_price,
        ROUND(MAX(price), 2) AS max_price,

        MIN(period_start_date) AS first_observation_date,
        MAX(period_end_date) AS last_observation_date

    FROM {{ ref('stg_food_prices') }}

    GROUP BY
        market_name,
        region_name,
        commodity_name,
        commodity_category,
        unit

),

latest_prices AS (

    SELECT
        market_name,
        commodity_name,
        unit,

        price AS latest_price,

        period_end_date AS latest_price_date,

        ROW_NUMBER() OVER (
            PARTITION BY
                market_name,
                commodity_name,
                unit
            ORDER BY
                period_end_date DESC
        ) AS row_num

    FROM {{ ref('stg_food_prices') }}

)

SELECT
    h.market_name,
    h.region_name,

    h.commodity_name,
    h.commodity_category,

    h.unit,

    h.total_records,

    h.avg_price,
    h.min_price,
    h.max_price,

    h.first_observation_date,
    h.last_observation_date,

    l.latest_price,
    l.latest_price_date

FROM market_history h

LEFT JOIN latest_prices l
    ON h.market_name = l.market_name
    AND h.commodity_name = l.commodity_name
    AND h.unit = l.unit

WHERE l.row_num = 1