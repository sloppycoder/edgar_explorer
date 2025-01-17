import gzip
import json
import logging
import os
from io import BytesIO

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError
from google.cloud import storage


class Command(BaseCommand):
    help = "Initialize the application by create users"

    def handle(self, *args, **options):
        admin_username = os.environ.get("ADMIN_USERNAME", "admin")
        admin_password = os.environ.get("ADMIN_PASSWORD", "admin")
        self.create_user(admin_username, admin_password)
        self.load_initial_data()

    def create_user(self, username, password):
        user = get_user_model()
        if user.objects.filter(username=username).count() > 0:
            print(f"User {username} already exists")
            return
        try:
            user.objects.create_superuser(username, "admin@@company.com", password)
            print(f"{username} user created with password {password}")
        except IntegrityError as e:
            print(f"Can't create user {username}, {e}")

    def load_initial_data(self):
        from edgar_explorer.apps import EdgarExplorerConfig

        seed_data_url = EdgarExplorerConfig.config["seed_data_url"]
        if seed_data_url.startswith("gs://"):
            load_filing_entries_from_gcs(seed_data_url)
        elif seed_data_url.startswith("postgresql://"):
            load_filing_entries_from_pg(seed_data_url)
        else:
            print(f"Unsupported seed data URL: {seed_data_url}")


def load_filing_entries_from_gcs(blob_url: str):
    from edgar_explorer.models import Filing

    bucket_name, blob_path = blob_url.replace("gs://", "").split("/", 1)
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(blob_path)

    if not blob.exists():
        print(f"Blob {blob_path} does not exist in bucket {bucket_name}.")
        return

    compressed_content = blob.download_as_bytes()
    decompressed_content = gzip.decompress(compressed_content)
    logging.info(f"Blob {blob_path} downloaded. Processing lines...")

    with BytesIO(decompressed_content) as decompressed_file:
        n_count = 0
        for line in decompressed_file:
            try:
                row = json.loads(line.decode("utf-8"))
                if "accession_number" not in row:
                    row["accession_number"] = (
                        row["filename"].replace(".txt", "").split("/")[-1]
                    )
                Filing.objects.create(**dict(row))
                n_count += 1
            except json.JSONDecodeError:
                continue

        print(f"Loaded {n_count} filings from {blob_url}")


def load_filing_entries_from_pg(database_url: str):
    import psycopg
    import psycopg.rows

    from edgar_explorer.models import Filing

    query = """
        SELECT DISTINCT
            idx.cik,
            company_name,
            form_type,
            TO_CHAR(date_filed, 'YYYY-MM-DD') as date_filed,
            idx_filename as filename,
            idx.accession_number,
            res.selected_chunks as chunks_used,
            res.selected_text as relevant_text,
            res.n_trustee as num_trustees,
            res.response as trustees_comp
        FROM master_idx_sample idx
        LEFT JOIN trustee_comp_results res
            ON res.cik = idx.cik
            AND res.accession_number = idx.accession_number
            AND 'orig225' = ANY(res.tags)
        WHERE 'orig225' = ANY(idx.tags)
        LIMIT 10000
    """
    try:
        with psycopg.connect(database_url) as connection:
            # Create a cursor that fetches rows as dictionaries
            with connection.cursor(row_factory=psycopg.rows.dict_row) as cursor:
                cursor.execute(query)
                for row in cursor:
                    Filing.objects.create(**row)
    except psycopg.Error as e:
        print(f"Database error: {e}")
        return []
    print(f"Loaded filings from {database_url}")
