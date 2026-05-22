from ingestion.clients.hdx_client import get_hdx_food_prices
from utils.logger import logger


def extract_sample_food_prices():
    """
    Extract sample food prices data from HDX API.
    """
    try:
        logger.info("Starting data extraction from HDX API...")

        params = {
            "location_code": "TZA",
            "admin1_name": "Mbeya",
            "commodity_name": "Tomatoes",
            "output_format": "json",
            "limit": 10,
            "offset": 0
        }

        response = get_hdx_food_prices(params)

        records = response.get("data", [])

        logger.info(f"Extracted {len(records)} records from HDX API.")

        return records

    except Exception as e:
        logger.error(f"Extraction failed: {e}")
        raise