import json
import re

import django_tables2 as tables
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.html import format_html
from django.views import View
from django_tables2 import SingleTableView

from .data_importer import dump_filings, load_filing_entries
from .models import Filing

PAGE_SIZE = 10


# class TruncatedTextColumn(tables.Column):
#     def render(self, value):
#         return value[:20] + "..." if len(value) > 20 else value


class FilingsTable(tables.Table):
    company_name = tables.Column(accessor="company_name", verbose_name="Company")
    responses = tables.Column(accessor="responses", verbose_name="Responses")
    info_type = tables.Column(accessor="info_type", verbose_name="Info Type")

    def render_company_name(self, value, record):
        if value:
            return value[:20] + "..." if len(value) > 20 else value
        return "N/A"

    def render_responses(self, value, record):
        response_count = len(record.responses) if record.responses else 0

        return format_html(
            '<a href="/filing/{}/">{}</a>',
            record.id,
            response_count,
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
            "responses",
            "accession_number",
            "info_type",
        )
        attrs = {"id": "filings-table", "class": "table table-striped"}
        orderable = False


class FilingsListView(LoginRequiredMixin, SingleTableView):
    model = Filing
    table_class = FilingsTable
    template_name = "extraction/filings_list.html"
    paginate_by = PAGE_SIZE

    def _filter_by_responses_count(self, queryset, operator, value):
        """Filter filings by responses count using comparison operator."""
        all_filings = list(queryset.all())
        filtered_filings = []

        for filing in all_filings:
            responses_count = len(filing.responses) if filing.responses else 0

            if operator == ">" and responses_count > value:
                filtered_filings.append(filing)
            elif operator == ">=" and responses_count >= value:
                filtered_filings.append(filing)
            elif operator == "<" and responses_count < value:
                filtered_filings.append(filing)
            elif operator == "<=" and responses_count <= value:
                filtered_filings.append(filing)
            elif operator == "=" and responses_count == value:
                filtered_filings.append(filing)

        if filtered_filings:
            filing_ids = [f.id for f in filtered_filings]
            return queryset.filter(id__in=filing_ids)
        return queryset.none()

    def get_queryset(self):
        queryset = super().get_queryset()
        sort_order = ["batch_id", "cik", "-date_filed"]

        search_term = self.request.GET.get("q")
        if search_term:
            search_term = search_term.strip()

        if not search_term:
            return queryset.all().order_by(*sort_order)[:10000]

        # Check for comparison operators for responses count
        comparison_match = re.match(r"^([><=]+)(\d+)$", search_term)
        if comparison_match:
            operator = comparison_match.group(1)
            value = int(comparison_match.group(2))
            queryset = self._filter_by_responses_count(queryset, operator, value)
        elif search_term.isdigit():
            queryset = queryset.filter(Q(cik__contains=search_term))
        elif len(search_term) == 20:
            queryset = queryset.filter(Q(accession_number=search_term))
        else:
            queryset = queryset.filter(Q(company_name__icontains=search_term))

        return queryset.order_by(*sort_order)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["q"] = self.request.GET.get("q", "")
        return context


def readiness_check(request):
    return JsonResponse({"status": "ok"})


def health_check(request):
    return JsonResponse({"status": "ok"})


class FilingDetailView(LoginRequiredMixin, View):
    def get(self, request, filing_id):
        filing = get_object_or_404(Filing, id=filing_id)

        context = {
            "filing": filing,
            "chunks": filing.chunks or [],
            "texts": json.dumps(filing.texts or []),
            "responses": json.dumps(filing.responses or []),
        }

        return render(request, "extraction/filing_detail.html", context)


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
