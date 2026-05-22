from ingestion.extract.food_prices_extractor import extract_sample_food_prices
from utils.logger import logger


def main():
    try:
        logger.info("Starting HDX extraction test...")

        records = extract_sample_food_prices()

        if records:
            logger.info(f"First commodity: {records[0]['commodity_name']}")

        logger.info("Extraction test completed successfully.")

    except Exception as e:
        logger.error(f"Pipeline execution failed: {e}")
        raise


if __name__ == "__main__":
    main()