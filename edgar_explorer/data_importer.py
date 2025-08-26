import json
import logging
import os
import sqlite3
import tempfile

from django.db import IntegrityError
from google.cloud import bigquery, storage

from .models import Filing


def load_filing_entries(batch_ids: list[str]) -> int:
    table = os.environ.get("RESULT_TABLE", "edgar.extraction_result")

    logging.info(f"Loading filings from {table} for batch IDs: {batch_ids}")

    # query records
    client = bigquery.Client(project="edgar-ai-dev")
    query = f"SELECT * FROM `{table}` WHERE batch_id IN UNNEST(@batch_ids) LIMIT 5000"  # noqa E501
    job_config = bigquery.QueryJobConfig(
        query_parameters=[bigquery.ArrayQueryParameter("batch_ids", "STRING", batch_ids)]
    )
    query_job = client.query(query, job_config=job_config)

    n_count = 0
    for row in query_job:
        responses = row["responses"]
        if not responses:
            continue

        chunks = []
        annotated_texts = []
        citation_positions = []
        for _, source_json in enumerate(row["sources"]):
            source = json.loads(source_json)
            chunks.append(source["ref"])
            citation_pos = source["citation_positions"]
            citation_positions.append(citation_pos)
            annotated_texts.append(_annotate_text(source["text"], citation_pos))

        try:
            Filing.objects.create(
                cik=row["cik"],
                company_name=row["company_name"],
                form_type="485BPOS",
                date_filed=row["date_filed"],
                accession_number=row["accession_number"],
                chunks=chunks,
                texts=annotated_texts,
                responses=responses,
                batch_id=row["batch_id"],
                info_type=row["extraction_type"],
                citation_positions=citation_positions,
                num_responses=len(responses),
                model=row.get("model"),
                cost=row.get("cost", 0.0),
            )
            n_count += 1
        except IntegrityError:
            logging.warning(
                f"Skipping duplicate filing: CIK={row['cik']}, Accession={row['accession_number']}, Batch={row['batch_id']}"  # noqa E501
            )

    logging.info(f"Loaded {n_count} filings from {table}")

    return n_count


def dump_filings():
    """
    Dumps the edgar_explorer_filing table to a Google Cloud Storage bucket.
    """
    from django.conf import settings

    bucket_name, blob_path = _db_file_path()
    if not bucket_name:
        return

    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(blob_path)

    with tempfile.NamedTemporaryFile(delete=True) as temp_file:
        logging.info(
            f"Dumping edgar_explorer_filing table to temporary file {temp_file.name}"
        )
        db_path = settings.DATABASES["default"]["NAME"]
        conn = sqlite3.connect(db_path)
        with open(temp_file.name, "w") as f:
            for line in conn.iterdump():
                if "edgar_explorer_filing" in line:
                    f.write(f"{line}\n")
        conn.close()

        logging.info(f"Uploading table dump to gs://{bucket_name}/{blob_path}")
        blob.upload_from_filename(temp_file.name)
        logging.info("Table dump upload complete.")


def load_filings():
    """
    Loads the edgar_explorer_filing table from a Google Cloud Storage bucket.
    """
    from django.conf import settings

    bucket_name, blob_path = _db_file_path()
    if not bucket_name:
        return

    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(blob_path)
    if not blob.exists():
        return

    try:
        with tempfile.NamedTemporaryFile(delete=True) as temp_file:
            logging.info(f"Downloading table dump from gs://{bucket_name}/{blob_path}")
            blob.download_to_filename(temp_file.name)

            logging.info(f"Restoring edgar_explorer_filing table from {temp_file.name}")
            db_path = settings.DATABASES["default"]["NAME"]
            conn = sqlite3.connect(db_path)
            with open(temp_file.name, "r") as f:
                sql_script = f.read()
            conn.execute("drop table edgar_explorer_filing")
            conn.executescript(sql_script)
            conn.close()
            logging.info("Table restore complete.")
    except Exception as e:
        logging.warning(f"Unable to restore database due to {e}")


def _db_file_path():
    # detect if running in Google Cloud Run
    # if not, return None so no database dump is created or loaded
    if not os.getenv("K_SERVICE"):
        return None, None

    gcs_path = os.environ.get(
        "DB_FILE_PATH", "gs://edgar_666/edgar_explorer/last_db_new.dump"
    )
    if gcs_path.endswith("/"):
        gcs_path = gcs_path[:-1]
    parts = gcs_path[5:].split("/", 1)
    if len(parts) != 2:
        raise ValueError(
            "GCS_DB_PATH must be in the format gs://bucket_name/path/to/file"
        )
    return parts[0], parts[1]


def _annotate_text(chunk_text: str, citation_pos: list[list[int]]) -> str:
    """
    Annotate text by inserting citation marks at specified positions.

    Args:
        chunk_text: Original text to annotate
        citation_pos: List of (start, end) tuples indicating citation positions

    Returns:
        Text with citation marks inserted
    """
    if not citation_pos:
        return chunk_text

    # Sort positions by start index in reverse order to avoid offset issues
    sorted_positions = sorted(citation_pos, key=lambda x: x[0], reverse=True)

    result = chunk_text
    for i, (start, end) in enumerate(sorted_positions):
        # Citation sequence number (reverse order, so adjust)
        citation_num = len(sorted_positions) - i

        # Insert end mark first, then start mark to avoid offset issues
        result = result[:end] + f"⸨/{citation_num}⸩ " + result[end:]
        result = result[:start] + f"⸨{citation_num}⸩ " + result[start:]

    return result
