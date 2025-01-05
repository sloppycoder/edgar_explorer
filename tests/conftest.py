from pathlib import Path

import pytest
from django.contrib.auth.models import User
from django.db import connection

TEST_USER = "test1"
TEST_PASSWORD = "test123"


@pytest.fixture(scope="function")
def authenticated_client(client, db):
    User.objects.create_user(username=TEST_USER, password=TEST_PASSWORD)
    client.login(username=TEST_USER, password=TEST_PASSWORD)
    yield client
    client.logout()


@pytest.fixture(scope="function", autouse=True)
def seed_database(db):
    django_conn = connection.cursor()

    with open(Path(__file__).parent / "data/seed.sql") as f:
        sql = f.read()
        django_conn.connection.executescript(sql)
