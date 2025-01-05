# load data from BigQuery into the models
import logging

from google.cloud import bigquery
from google.cloud.bigquery.job import QueryJob


def run_query(query: str) -> QueryJob:
    """
    Run a query in BigQuery

    Args:
        query (str): The BigQuery query to execute

    Returns:
        QueryJob: The query job object
    """
    with bigquery.Client() as bq_client:
        query_job = bq_client.query(query)
        query_job.result()
        elapsed_t = query_job.ended - query_job.started
        logging.debug(f"query -> {query[:200]} took {elapsed_t.total_seconds()} seconds")
        return query_job


def load_filing_entries(dataset_id, **kwargs) -> None:
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

    job = run_query(query)
    filings = [Filing.objects.create(**dict(row)) for row in job]

    logging.info(f"Loaded {len(filings)} from BigQuery")
