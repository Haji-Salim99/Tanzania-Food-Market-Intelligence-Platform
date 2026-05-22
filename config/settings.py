import os
from dotenv import load_dotenv

load_dotenv()

HDX_APP_IDENTIFIER = os.getenv("HDX_APP_IDENTIFIER")
HDX_BASE_URL = os.getenv("HDX_BASE_URL")
GCP_PROJECT_ID = os.getenv("GCP_PROJECT_ID")
GCP_DATASET= os.getenv("GCP_DATASET")
GOOGLE_APPLICATION_CREDENTIALS = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
COUNTRY_CODE = os.getenv("COUNTRY_CODE")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
DATASET_LOCATION = os.getenv("DATASET_LOCATION", "africa-south1")
FOOD_PRICES_ENDPOINT = os.getenv("FOOD_PRICES_ENDPOINT")
