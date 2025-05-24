import json

import django_tables2 as tables
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.utils.html import format_html
from django.views import View
from django_tables2 import SingleTableView

from .data_importer import dump_filings, load_filing_entries
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
        if record.info_type == "trustee":
            data_type = "trustee"
        else:
            data_type = "fundmgr"

        return format_html(
            '<a href="#" data-bs-toggle="modal"'
            + f'data-type="{data_type}"'
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

    def render_batch_id(self, value, record):
        return value.split("-")[1] if value else ""

    class Meta:
        model = Filing
        template_name = "django_tables2/bootstrap5.html"
        fields = (
            "batch_id",
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
    template_name = "extraction/filings_list.html"
    paginate_by = PAGE_SIZE

    def get_queryset(self):
        queryset = super().get_queryset()
        sort_order = ["batch_id", "cik", "-date_filed"]

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


class LoadNewDataView(LoginRequiredMixin, View):
    def post(self, request):
        batch_ids = request.POST.get("batch_ids", "")
        if not batch_ids:
            messages.error(request, "Batch IDs cannot be empty.")
            return redirect("load_new")

        batch_ids_list = [
            batch_id.strip() for batch_id in batch_ids.split(",") if batch_id.strip()
        ]

        if not batch_ids_list:
            messages.error(request, "Invalid Batch IDs provided.")
            return redirect("load_new")

        clear_all = request.POST.get("clear_all", "off") == "on"
        if clear_all:
            try:
                Filing.objects.all().delete()
            except Exception as e:
                messages.error(request, f"Error clearing data: {str(e)}")
                return redirect("load_new")
        else:
            Filing.objects.filter(batch_id__in=batch_ids).delete()

        try:
            n_loaded = load_filing_entries(batch_ids_list)
            if n_loaded > 0:
                dump_filings()
            messages.success(
                request,
                f"Successfully loaded {n_loaded} entries for Batch IDs: {', '.join(batch_ids_list)}",  # noqa E501
            )
        except Exception as e:
            messages.error(request, f"Error loading data: {str(e)}")

        return redirect("listing")

    def get(self, request):
        return render(request, "extraction/load_new.html")
