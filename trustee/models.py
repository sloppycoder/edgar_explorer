from django.db import models


class FilingIndexEntry(models.Model):
    cik = models.CharField(max_length=10)
    company_name = models.CharField(max_length=150)
    form_type = models.CharField(max_length=20)
    date_filed = models.CharField(max_length=10)
    filename = models.CharField(max_length=100)
    accession_number = models.CharField(max_length=20)
