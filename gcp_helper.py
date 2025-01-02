import logging
import os

from google.cloud import logging as cloud_logging

logger = logging.getLogger(__name__)


def setup_cloud_logging():
    if os.getenv("K_SERVICE"):  # Only initialize Google Cloud Logging in Cloud Run
        client = cloud_logging.Client()
        client.setup_logging()
        logging.info("Google Cloud Logging is set up.")
    else:
        logging.basicConfig(level=logging.INFO)
        logging.info("Running locally. Using basic logging.")
