import django_tables2 as tables
from django.http import JsonResponse
from django_tables2 import SingleTableView

from .models import FilingIndexEntry

PAGE_SIZE = 15


class FilingsTable(tables.Table):
    class Meta:
        model = FilingIndexEntry
        template_name = "django_tables2/bootstrap5.html"
        fields = ("cik", "company_name", "date_filed")


class FilingsListView(SingleTableView):
    model = FilingIndexEntry
    table_class = FilingsTable
    template_name = "filings_list.html"


def readiness_check(request):
    return JsonResponse({"status": "ok"})


def health_check(request):
    return JsonResponse({"status": "ok"})
