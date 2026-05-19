from google.cloud import bigquery
from config.settings import GCP_PROJECT_ID
from utils.logger import logger


def get_bigquery_client():
    """
    Create authenticated BigQuery client.
    """
    try:
        client = bigquery.Client(project=GCP_PROJECT_ID)

        logger.info("BigQuery client authenticated successfully.")

        return client

    except Exception as e:
        logger.error(f"BigQuery connection failed: {e}")
        raise