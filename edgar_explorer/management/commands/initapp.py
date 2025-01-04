import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError


class Command(BaseCommand):
    help = "Initialize the application by create users"

    def handle(self, *args, **options):
        admin_username = os.environ.get("ADMIN_USERNAME", "admin")
        admin_password = os.environ.get("ADMIN_PASSWORD", "admin")
        self.create_user(admin_username, admin_password)
        self.load_initial_data()

    def create_user(self, username, password):
        user = get_user_model()
        if user.objects.filter(username=username).count() > 0:
            print(f"User {username} already exists")
            return
        try:
            user.objects.create_superuser(username, "admin@@company.com", password)
            print(f"{username} user created with password {password}")
        except IntegrityError as e:
            print(f"Can't create user {username}, {e}")

    def load_initial_data(self):
        from edgar_explorer.apps import FilingExplorerConfig
        from edgar_explorer.bq_adapter import load_filing_entries

        dateset_id = FilingExplorerConfig.config["dataset_id"]
        load_filing_entries(dateset_id)
