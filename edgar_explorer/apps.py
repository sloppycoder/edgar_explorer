import os

from django.apps import AppConfig


class FilingExplorerConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "edgar_explorer"
    config = {
        "dataset_id": os.environ.get("DATASET_ID", "edgar"),
    }
