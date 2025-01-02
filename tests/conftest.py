import asyncio
import logging
import os

import pytest

from gui import models as m
# suppress INFO logs to reduce noise in test output
root_logger = logging.getLogger()
root_logger.setLevel(logging.WARN)

@pytest.fixture(scope="session")
def event_loop():
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session")
def test_db(request, event_loop):
    import tortoise.contrib.test as tortoise_test
    from tortoise import Tortoise

    test_db_url = os.environ.get("TEST_DATABASE_URL", "sqlite://:memory:")
    tortoise_test._TORTOISE_TEST_DB = test_db_url
    config = tortoise_test.getDBConfig(app_label="models", modules=["gui.models"])
    event_loop.run_until_complete(tortoise_test._init_db(config))
    event_loop.run_until_complete(seed_db())

    if os.environ.get("KEEP_TEST_DB", "N").upper() not in ["Y", "1"]:
        request.addfinalizer(
            lambda: event_loop.run_until_complete(Tortoise._drop_databases())
        )


async def seed_db():
    await m.User(login_name = "root").save()
