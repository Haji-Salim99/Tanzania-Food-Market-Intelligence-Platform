SELECT
    region_name,
    
    commodity_code,
    commodity_name,
    commodity_category,
    unit,
    
    COUNT(*) AS total_records,

    ROUND(AVG(price),2) AS avg_price,
    ROUND(MIN(price),2) AS min_price,
    ROUND(MAX(price),2) AS max_price,

    COUNT(DISTINCT market_name) AS market_count

    FROM {{ ref('stg_food_prices') }}

    GROUP BY 
    region_name, 
    commodity_code, 
    commodity_name, 
    commodity_category,
    unit