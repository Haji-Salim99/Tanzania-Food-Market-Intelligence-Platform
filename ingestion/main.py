from ingestion.clients.bigquery_client import get_bigquery_client
from utils.logger import logger


def main():
    try:
        logger.info("Testing BigQuery connection...")

        client = get_bigquery_client()

        projects = list(client.list_projects())

        logger.info(f"Accessible projects found: {len(projects)}")

    except Exception as e:
        logger.error(f"Pipeline startup failed: {e}")
        raise


if __name__ == "__main__":
    main()