from utils.logger import logger
from ingestion.load.bigquery_loader import create_bigquery_dataset_if_not_exists


def main():
    try:
        logger.info("Starting infrastructure setup...")

        create_bigquery_dataset_if_not_exists()

        logger.info("Infrastructure setup completed successfully.")

    except Exception as e:
        logger.error(f"Infrastructure setup failed: {e}")
        raise 


if __name__ == "__main__":
    main()