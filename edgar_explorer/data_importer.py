import json
import logging
import os

from google.cloud import bigquery

from .models import Filing


def load_filing_entries(batch_ids: list[str]) -> int:
    table = os.environ.get("RESULT_TABLE", "edgar-ai.edgar2.extraction_result")

    logging.info(f"Loading filings from {table} for batch IDs: {batch_ids}")

    # Delete existing records in the Filing model
    Filing.objects.filter(batch_id__in=batch_ids).delete()

    # query records
    client = bigquery.Client()
    query = f"SELECT * FROM `{table}` WHERE batch_id IN UNNEST(@batch_ids) LIMIT 5000"
    job_config = bigquery.QueryJobConfig(
        query_parameters=[bigquery.ArrayQueryParameter("batch_ids", "STRING", batch_ids)]
    )
    query_job = client.query(query, job_config=job_config)

    n_count = 0
    num_entities = 0
    for row in query_job:
        try:
            info = json.loads(row["response"])
            if row["extraction_type"] == "trustee_comp":
                if info["compensation_info_present"]:
                    num_entities = len(info["trustees"])
            elif row["extraction_type"] == "fundmgr":
                num_entities = len(info["managers"])
            else:
                continue
        except json.JSONDecodeError:
            pass

        Filing.objects.create(
            cik=row["cik"],
            company_name="Some Company",
            form_type="485BPOS",
            date_filed=row["date_filed"],
            accession_number=row["accession_number"],
            chunks_used=row["selected_chunks"],
            relevant_text=row["selected_text"],
            num_entities=num_entities,
            info=row["response"],
            batch_id=row["batch_id"],
        )
        n_count += 1

    logging.info(f"Loaded {n_count} filings from {table}")

    return n_count
