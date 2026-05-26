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


def load_food_prices(records:list):
 
     #Load raw food price records into BigQuery

    try:
        if not records:
            logger.info("No records to load into BigQuery.")
            return

        client = get_bigquery_client()
        table_id = f"{GCP_PROJECT_ID}.{GCP_DATASET}.raw_food_prices"
        logger.info(f"Loading {len(records)} records into BigQuery table '{table_id}'...")

        job_config = bigquery.LoadJobConfig(
        write_disposition = bigquery.WriteDisposition.WRITE_APPEND,
        autodetect=True
     )
        load_job = client.load_table_from_json(
        records,
        table_id,
        job_config=job_config
        )

        load_job.result()  # Wait for the job to complete.

        logger.info(f"Successfully loaded {len(records)} records into BigQuery.")

    except Exception as e:
        logger.error(f"Failed to load records into BigQuery: {e}")
        raise