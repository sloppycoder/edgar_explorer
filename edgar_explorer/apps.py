import os

from django.apps import AppConfig


class EdgarExplorerConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "edgar_explorer"
    config = {
        "seed_data_url": os.environ.get(
            "SEED_DATA_URL", "gs://edgar_666/edgar_explorer/seed_data.jsonl.gz"
        ),
    }
