from ingestion.clients.hdx_client import get_hdx_food_prices
from config.settings import COUNTRY_CODE
from utils.logger import logger


def get_tanzania_regions():
    """
    Discover Tanzania regions from food prices dataset.
    """
    try:
        logger.info("Discovering Tanzania regions from food prices data...")

        params = {
            "location_code": COUNTRY_CODE,
            "commodity_category": "vegetables and fruits",
            "output_format": "json",
            "limit": 1000,
            "offset": 0
        }

        response = get_hdx_food_prices(params)

        records = response.get("data", [])

        regions = sorted(
            list(
                {
                    record["admin1_name"]
                    for record in records
                    if record.get("admin1_name")
                }
            )
        )

        logger.info(f"Discovered {len(regions)} regions.")

        return regions

    except Exception as e:
        logger.error(f"Failed to discover regions: {e}")
        raise