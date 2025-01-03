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

    def create_user(self, username, password):
        user = get_user_model()
        if user.objects.filter(username=username).count() > 0:
            print(f"User {username} already exists")
            return
        try:
            user.objects.create_superuser(username, "admin@@company.com", password)
            print(f"{username} user created")
        except IntegrityError as e:
            print(f"Can't create user {username}, {e}")
