import json
import logging
import os
import sqlite3
import tempfile

from django.db import IntegrityError
from google.cloud import firestore, storage
from google.cloud.firestore_v1.base_query import FieldFilter

from .models import Filing


def load_filing_entries(batch_ids: list[str]) -> int:
    collection_name = os.environ.get("EXTRACTION_RESULT_COLLECTION", "extraction_result")

    logging.info(f"Loading filings from '{collection_name}' for batch IDs: {batch_ids}")

    # query records
    client = firestore.Client()
    collection_ref = client.collection(collection_name)
    query = collection_ref.where(
        filter=FieldFilter(
            "batch_id",
            "in",
            batch_ids,
        )
    ).limit(5000)
    docs = query.stream()

    n_count = 0
    for doc in docs:
        row = doc.to_dict()
        num_entities = 0
        try:
            info = json.loads(row["response"])
            if row["extraction_type"] == "trustee":
                if info["compensation_info_present"]:
                    num_entities = len(info["trustees"])
            elif row["extraction_type"] == "fundmgr":
                num_entities = len(info["managers"])
            else:
                continue
        except json.JSONDecodeError:
            pass

        try:
            Filing.objects.create(
                cik=row["cik"],
                company_name=row["company_name"],
                form_type="485BPOS",
                date_filed=row["date_filed"],
                accession_number=row["accession_number"],
                chunks_used=row["selected_chunks"],
                relevant_text=row["selected_text"],
                num_entities=num_entities,
                info=row["response"],
                batch_id=row["batch_id"],
                info_type=row["extraction_type"],
            )
            n_count += 1
        except IntegrityError:
            logging.warning(
                f"Skipping duplicate filing: CIK={row['cik']}, Accession={row['accession_number']}, Batch={row['batch_id']}"  # noqa E501
            )

    logging.info(
        f"Loaded {n_count} filings from Firestore collection '{collection_name}'"
    )

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

    with tempfile.NamedTemporaryFile(delete=True) as temp_file:
        logging.info(f"Downloading table dump from gs://{bucket_name}/{blob_path}")
        blob.download_to_filename(temp_file.name)

        logging.info(
            f"Restoring edgar_explorer_filing table from temporary file {temp_file.name}"
        )
        db_path = settings.DATABASES["default"]["NAME"]
        conn = sqlite3.connect(db_path)
        with open(temp_file.name, "r") as f:
            sql_script = f.read()
        conn.execute("drop table edgar_explorer_filing")
        conn.executescript(sql_script)
        conn.close()
        logging.info("Table restore complete.")


def _db_file_path():
    # detect if running in Google Cloud Run
    # if not, return None so no database dump is created or loaded
    if not os.getenv("K_SERVICE"):
        return None, None

    gcs_path = os.environ.get(
        "DB_FILE_PATH", "gs://edgar_666/edgar_explorer/last_db.dump"
    )
    if gcs_path.endswith("/"):
        gcs_path = gcs_path[:-1]
    parts = gcs_path[5:].split("/", 1)
    if len(parts) != 2:
        raise ValueError(
            "GCS_DB_PATH must be in the format gs://bucket_name/path/to/file"
        )
    return parts[0], parts[1]
