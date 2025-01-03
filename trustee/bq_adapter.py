# load data from BigQuery into the models
from google.cloud import bigquery


def query_to_model(model, query: str) -> None:
    """
    Load data from BigQuery into a Django model.

    Args:
        model (django.db.models.Model): The Django model to load data into.
        query (str): The BigQuery query to execute
    """
    # Get the BigQuery client
    with bigquery.Client() as bq_client:
        job = bq_client.query(query)
        job.result()

        for row in job:
            obj = model.objects.create(**dict(row))
            obj.save()


def load_filing_entries(sender, **kwargs):
    from .models import Filing

    # load data from BigQuery into Filing models
    dataset_id = sender.config["dataset_id"]
    query = f"""
        SELECT
            cik,
            company_name,
            form_type,
            date_filed,
            filename,
            accession_number
        FROM {dataset_id}.master_idx_sample
        LIMIT 10000
        """
    query_to_model(Filing, query)
