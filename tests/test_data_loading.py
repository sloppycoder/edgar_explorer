import pytest  # noqa F401
from edgar_explorer.data_importer import load_filing_entries
from edgar_explorer.models import Filing


# @pytest.mark.skip(reason="for local use only")
def test_load_data_from_bigquery():
    batch_id = "20250419094434-acp"
    n_loaded = load_filing_entries([batch_id])
    filings = Filing.objects.filter(batch_id=batch_id)  # pyright: ignore
    assert len(filings) == n_loaded
