from django.db import models


class Filing(models.Model):
    class Meta:
        verbose_name = "SEC Filing in Master Index"
        verbose_name_plural = "SEC Filings in Master Index"
        constraints = [
            models.UniqueConstraint(
                fields=["cik", "accession_number", "batch_id"],
                name="unique_filing_constraint",
            )
        ]

    cik = models.CharField(max_length=10, verbose_name="CIK")
    company_name = models.CharField(max_length=150, verbose_name="Company Name")
    form_type = models.CharField(max_length=20, verbose_name="Form Type")
    date_filed = models.CharField(max_length=10, verbose_name="Date Filed")
    accession_number = models.CharField(max_length=20, verbose_name="Accession Number")
    chunks = models.JSONField(default=list, verbose_name="Chunk Numbers", null=True)
    texts = models.JSONField(default=list, verbose_name="Chunk Texts", null=True)
    responses = models.JSONField(default=list, verbose_name="Responses", null=True)
    batch_id = models.CharField(max_length=20, verbose_name="Batch ID", null=True)
    info_type = models.CharField(
        max_length=16, verbose_name="Information Type", null=True
    )
    citation_positions = models.JSONField(
        default=list, verbose_name="Citation Positions", null=True
    )
    num_responses = models.IntegerField(default=0, verbose_name="Number of Responses")
