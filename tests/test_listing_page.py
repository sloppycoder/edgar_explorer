import pytest
from bs4 import BeautifulSoup


@pytest.mark.django_db
def test_filing_blank_search(authenticated_client):
    client = authenticated_client
    response = client.get("/")
    assert response.status_code == 200, "Unable to load home page"

    soup = BeautifulSoup(response.content, "html.parser")
    assert soup.find("h2").text == "Processed Filings"  # type: ignore

    table = soup.find("table", id="filings-table")
    assert table is not None

    # Find all rows in the table
    rows = table.find_all("tr")  # type: ignore
    assert len(rows) > 1, "Table shouldn't be empty"
