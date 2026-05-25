from config.constants import TANZANIA_REGIONS
from ingestion.extract.food_prices_extractor import extract_food_prices
from ingestion.load.bigquery_loader import (
    create_bigquery_dataset_if_not_exists,
    load_food_prices
)
from utils.logger import logger


def main():
    try:
        logger.info("Starting regional extraction test...")

        create_bigquery_dataset_if_not_exists()

        test_regions = TANZANIA_REGIONS[:2]

        for region in test_regions:
            logger.info(f"Processing region: {region}")

            offset = 0
            total_region_records = 0

            while True:
                records = extract_food_prices(
                    region_name=region,
                    limit=1000,
                    offset=offset
                )

                if not records:
                    logger.info(f"No more records for {region}")
                    break

                load_food_prices(records)

                total_region_records += len(records)

                offset += 1000

            logger.info(
                f"Completed {region}: {total_region_records} total records"
            )

        logger.info("Extraction + load pipeline completed successfully.")

    except Exception as e:
        logger.error(f"Pipeline execution failed: {e}")
        raise


if __name__ == "__main__":
    main()