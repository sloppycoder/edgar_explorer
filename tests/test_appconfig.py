import time

import pytest


@pytest.mark.django_db
def test_appconfig_ready(client):
    time.sleep(5)
    response = client.get("/")
    assert response.status_code == 200, "Homepage did not load correctly."
