SELECT
    CAST(location_code AS STRING) AS location_code,
    CAST(location_name AS STRING) AS location_name,

    CAST(admin1_code AS STRING) AS region_code,
    CAST(admin1_name AS STRING) AS region_name,

    CAST(admin2_code AS STRING) AS district_code,
    CAST(admin2_name AS STRING) AS district_name,

    CAST(market_code AS STRING) AS market_code,
    CAST(market_name AS STRING) AS market_name,

    CAST(commodity_code AS STRING) AS commodity_code,
    CAST(commodity_name AS STRING) AS commodity_name,
    CAST(commodity_category AS STRING) AS commodity_category,

    CAST(currency_code AS STRING) AS currency_code,
    CAST(unit AS STRING) AS unit,

    CAST(price_type AS STRING) AS price_type,
    CAST(price_flag AS STRING) AS price_flag,

    CAST(price AS FLOAT64) AS price,

    CAST(lat AS FLOAT64) AS latitude,
    CAST(lon AS FLOAT64) AS longitude,

    CAST(reference_period_start AS TIMESTAMP) AS period_start_date,
    CAST(reference_period_end AS TIMESTAMP) AS period_end_date,

    CAST(resource_hdx_id AS STRING) AS resource_hdx_id

FROM {{ source('food_market_raw', 'raw_food_prices') }}