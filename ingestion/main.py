from ingestion.extract.admin_extractor import get_tanzania_regions
from utils.logger import logger


def main():
    try:
        logger.info("Starting Tanzania region discovery test...")

        regions = get_tanzania_regions()

        logger.info(f"Sample regions: {regions[:5]}")

        logger.info("Region discovery completed successfully")

    except Exception as e:
        logger.error(f"Pipeline execution failed: {e}")
        raise


if __name__ == "__main__":
    main()