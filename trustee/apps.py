import os

from django.apps import AppConfig
from django.db.models.signals import post_migrate

from .bq_adapter import load_filing_entries


class TrusteeConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "trustee"
    site_name = "trustee"  # has to hardcode. there's no other way to find out
    config = {
        "dataset_id": os.environ.get("DATASET_ID", "edgar_dev"),
    }

    def ready(self):
        post_migrate.connect(load_filing_entries, sender=self)
