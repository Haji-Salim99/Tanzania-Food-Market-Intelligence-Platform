from ingestion.clients.hdx_client import get_hdx_food_prices
from config.settings import COUNTRY_CODE
from utils.logger import logger



def extract_food_prices(region_name: str, limit: int = 1000, offset: int = 0):
    """
    Extract sample food prices data from HDX API.
    """
    try:
        logger.info(f"Extracting region={region_name}, limit={limit}, offset={offset}")

        params = {
            "location_code": COUNTRY_CODE,
            "admin1_name": region_name,
            "output_format": "json",
            "limit": limit,
            "offset": offset
        }

        response = get_hdx_food_prices(params)

        records = response.get("data", [])

        logger.info(f"Fetched {len(records)} records for region={region_name}")
    
        return records

    except Exception as e:
        logger.error(f"Extraction failed: {e}")
        raise