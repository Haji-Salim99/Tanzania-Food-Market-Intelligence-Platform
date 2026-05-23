import requests
from config.settings import HDX_BASE_URL, HDX_APP_IDENTIFIER
from utils.logger import logger


def hdx_get(endpoint: str, params: dict):
    """
    Generic HDX GET request helper.
    """
    try:
        url = f"{HDX_BASE_URL}{endpoint}"

        headers = {
            "accept": "application/json"
        }

        params["app_identifier"] = HDX_APP_IDENTIFIER

        response = requests.get(
            url=url,
            headers=headers,
            params=params,
            timeout=30
        )

        response.raise_for_status()

        logger.info(f"HDX request successful: {endpoint}")

        return response.json()

    except requests.exceptions.RequestException as e:
        logger.error(f"HDX request failed: {e}")
        raise


def get_hdx_food_prices(params: dict):
    """
    Food prices endpoint wrapper.
    """
    endpoint = "/food-security-nutrition-poverty/food-prices-market-monitor"

    return hdx_get(endpoint, params)