from django.db import models


class Filing(models.Model):
    class Meta:
        verbose_name = "SEC Filing in Master Index"
        verbose_name_plural = "SEC Filings in Master Index"

    cik = models.CharField(max_length=10, verbose_name="CIK")
    company_name = models.CharField(max_length=150, verbose_name="Company Name")
    form_type = models.CharField(max_length=20, verbose_name="Form Type")
    date_filed = models.CharField(max_length=10, verbose_name="Date Filed")
    filename = models.CharField(max_length=100, verbose_name="EDGAR file name")
    accession_number = models.CharField(max_length=20, verbose_name="Accession Number")
    chunks_used = models.CharField(max_length=100, verbose_name="Chunks", null=True)
    relevant_text = models.CharField(max_length=8192, verbose_name="Chunks", null=True)
    num_trustees = models.IntegerField(verbose_name="Trustees", null=True)
    trustees_comp = models.CharField(
        max_length=4096, verbose_name="Trustees Compensation", null=True
    )
    batch_id = models.CharField(max_length=20, verbose_name="Batch ID", null=True)
