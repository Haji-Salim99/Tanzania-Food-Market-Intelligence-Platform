import requests
from config.settings import HDX_APP_IDENTIFIER, HDX_BASE_URL, FOOD_PRICES_ENDPOINT
from utils.logger import logger

def get_hdx_food_prices(params: dict):
    """Fetch food prices data from HDX HAPI API."""
    try:
        url = f"{HDX_BASE_URL}{FOOD_PRICES_ENDPOINT}"

        headers = {
            "accept": "application/json",
        }

        params["app_identifier"] = HDX_APP_IDENTIFIER

        response = requests.get(
            url=url,
            headers=headers,
            params=params,
            timeout=30,
        )

        response.raise_for_status()

        logger.info("HDX API request successful.")

        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"HDX API request failed: {e}")
        raise
     

