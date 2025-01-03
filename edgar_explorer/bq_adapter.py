# load data from BigQuery into the models
import logging

from google.cloud import bigquery


def query_to_model(model, query: str) -> int:
    """
    Load data from BigQuery into a Django model.

    Args:
        model (django.db.models.Model): The Django model to load data into.
        query (str): The BigQuery query to execute
    """
    # Get the BigQuery client
    with bigquery.Client() as bq_client:
        job = bq_client.query(query)
        models = [model.objects.create(**dict(row)) for row in job]
        logging.info(f"Loaded {len(models)} rows into {model.__name__}")


def load_filing_entries(dataset_id, **kwargs):
    from .models import Filing

    logging.info("Loading data from BigQuery...")

    # load data from BigQuery into Filing models
    query = f"""
        SELECT DISTINCT
            idx.cik,
            company_name,
            form_type,
            date_filed,
            filename,
            idx.accession_number,
            res.chunk_nums as chunks_used,
            res.relevant_text as relevant_text,
            res.n_trustee as num_trustees,
            res.model_response as trustees_comp
        FROM `{dataset_id}.master_idx_sample` idx
        LEFT JOIN `{dataset_id}.trustee_comp_results` res
        ON res.cik = idx.cik
        AND res.accession_number = idx.accession_number
        LIMIT 10000
        """
    logging.info("Calling query_to_model")
    query_to_model(Filing, query)
    logging.info("Done query_to_model")
