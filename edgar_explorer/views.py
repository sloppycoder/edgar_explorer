import json

import django_tables2 as tables
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import JsonResponse
from django.utils.html import format_html
from django_tables2 import SingleTableView

from .models import Filing

PAGE_SIZE = 10


class TruncatedTextColumn(tables.Column):
    def render(self, value):
        return value[:20] + "..." if len(value) > 20 else value


class FilingsTable(tables.Table):
    company_name = TruncatedTextColumn(verbose_name="Company Name")

    # this somehow doesn't work...
    # def render_company_name(self, value, _):
    #     if value:
    #         return value[:20] + "..." if len(value) > 20 else value
    #     return "N/A"

    def render_num_entities(self, value, record):
        return format_html(
            '<a href="#" data-bs-toggle="modal"  data-type="trustee"'
            + f'data-bs-target="#genericModal" data-info="{{}}">{value}</a>',
            record.info,
        )

    def render_chunks_used(self, value, record):
        data = json.dumps(
            {
                "chunk_nums": value,
                "relevant_text": record.relevant_text,
            }
        )
        return format_html(
            '<a href="#" data-bs-toggle="modal"  data-type="chunk"'
            + f'data-bs-target="#genericModal" data-info="{{}}">{value}</a>',
            data,
        )

    def render_accession_number(self, value, record):
        # navigate to the SEC page for the filing
        # filename: edgar/data/105563/0001683863-24-001950.txt
        # URL path edgar/data/105563/000168386324001950/0001683863-24-001950-index.html
        # this logic may not work for older filings, e.g. pre 2004
        sn = record.accession_number
        path = f"edgar/data/{record.cik}/{sn.replace("-","")}/{sn}-index.html"
        return format_html(
            f'<a href="https://www.sec.gov/Archives/{path}" target="_blank">{value}</a>',
            value,
        )

    class Meta:
        model = Filing
        template_name = "django_tables2/bootstrap5.html"
        fields = (
            "cik",
            "company_name",
            "date_filed",
            "chunks_used",
            "num_entities",
            "accession_number",
        )
        attrs = {"id": "filings-table", "class": "table table-striped"}
        orderable = False


class FilingsListView(LoginRequiredMixin, SingleTableView):
    model = Filing
    table_class = FilingsTable
    template_name = "trustee/filings_list.html"
    paginate_by = PAGE_SIZE

    def get_queryset(self):
        queryset = super().get_queryset()
        sort_order = ["cik", "-date_filed"]

        search_term = self.request.GET.get("q")
        if not search_term:
            queryset = queryset.all().order_by(*sort_order)[:1000]
        elif search_term.isdigit():
            queryset = queryset.filter(
                Q(cik__contains=search_term),
            ).order_by(*sort_order)
        elif len(search_term) == 20:
            queryset = queryset.filter(
                Q(accession_number=search_term),
            ).order_by(*sort_order)
        else:
            queryset = queryset.filter(
                Q(company_name__icontains=search_term),
            ).order_by(*sort_order)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["q"] = self.request.GET.get("q", "")
        return context


def readiness_check(request):
    return JsonResponse({"status": "ok"})


def health_check(request):
    return JsonResponse({"status": "ok"})
