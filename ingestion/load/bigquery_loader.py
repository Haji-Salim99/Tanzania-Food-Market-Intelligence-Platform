from google.cloud import bigquery
from config.settings import GCP_PROJECT_ID, GCP_DATASET, DATASET_LOCATION
from utils.logger import logger
from ingestion.clients.bigquery_client import get_bigquery_client

def create_bigquery_dataset_if_not_exists():
    try:
        client = get_bigquery_client()
        dataset_id = f"{GCP_PROJECT_ID}.{GCP_DATASET}"
        dataset = bigquery.Dataset(dataset_id)
        dataset.location = DATASET_LOCATION
        client.create_dataset(dataset, exists_ok=True)
        
        logger.info(f"BigQuery dataset '{dataset_id}' is ready.")

    except Exception as e:
        logger.error(f"Failed to create BigQuery dataset: {e}")
        raise
