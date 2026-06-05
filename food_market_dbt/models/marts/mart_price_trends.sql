SELECT
    DATE_TRUNC(
        DATE(period_start_date),
        MONTH
    ) AS month_start_date,

    region_name,
    commodity_name,
    commodity_category,
    unit,

    COUNT(*) AS total_records,

    ROUND(AVG(price),2) AS avg_price,
    ROUND(MIN(price),2) AS min_price,
    ROUND(MAX(price),2) AS max_price

    FROM {{ref('stg_food_prices') }}

    GROUP BY
    month_start_date,
    region_name,
    commodity_name,
    commodity_category,
    unit
