import os

from django.apps import AppConfig


class TrusteeConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "trustee"
    site_name = "trustee"  # has to hardcode. there's no other way to find out
    config = {
        "dataset_id": os.environ.get("DATASET_ID", "edgar"),
    }
