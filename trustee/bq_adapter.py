# load data from BigQuery into the models
import logging

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
            row_dict = dict(row)
            # print(row_dict)
            obj = model.objects.create(**row_dict)
            obj.save()


def load_filing_entries(sender, **kwargs):
    from .models import Filing

    logging.info("Loading data from BigQuery...")

    # load data from BigQuery into Filing models
    dataset_id = sender.config["dataset_id"]
    query = f"""
        SELECT
            idx.cik,
            company_name,
            form_type,
            date_filed,
            filename,
            idx.accession_number,
            '12,34' as chunks_used,
            res.n_trustee as num_trustees,
            res.json_text as trustees_comp
        FROM `{dataset_id}.master_idx_sample` idx
        LEFT JOIN `{dataset_id}.trustee_comp_results` res
        ON res.cik = idx.cik
        AND res.accession_number = idx.accession_number
        LIMIT 10000
        """
    query_to_model(Filing, query)
