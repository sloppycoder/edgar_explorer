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
    batch_id = tables.Column(accessor="batch_id", verbose_name="ID")
    company_name = tables.Column(accessor="company_name", verbose_name="Company")
    responses = tables.Column(accessor="responses", verbose_name="Responses")
    model = tables.Column(accessor="model", verbose_name="Model")
    info_type = tables.Column(accessor="info_type", verbose_name="Info Type")
    batch_date = tables.Column(accessor="batch_id", verbose_name="Date")
    cost = tables.Column(accessor="cost", verbose_name="Cost")

    def render_company_name(self, value, record):
        if value:
            return value[:20] + "..." if len(value) > 20 else value
        return "N/A"

    def render_responses(self, value, record):
        from urllib.parse import quote, urlencode

        request = getattr(self, "request", None)
        query_string = ""
        if request and request.GET:
            query_string = "?" + urlencode(request.GET)

        back_url = f"/{query_string}" if query_string else "/"

        return format_html(
            '<a href="/filing/{}/?back_url={}">{}</a>',
            record.id,
            quote(back_url, safe=""),
            record.num_responses,
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

    def render_batch_date(self, value, record):
        if not value:
            return ""
        # Extract timestamp part (before the dash)
        timestamp_part = value.split("-")[0] if "-" in value else value
        if len(timestamp_part) >= 12:  # YYYYMMDDHHMM format
            try:
                month = timestamp_part[4:6]
                day = timestamp_part[6:8]
                hour = timestamp_part[8:10]
                minute = timestamp_part[10:12]
                return f"{month}/{day} {hour}:{minute}"
            except (ValueError, IndexError):
                return value
        return value

    def render_model(self, value, record):
        if value and "/" in value:
            return value.split("/")[-1]
        return value or ""

    def render_cost(self, value, record):
        if value is not None:
            return f"${value:.2f}"
        return "$0.00"

    class Meta:
        model = Filing
        template_name = "django_tables2/bootstrap5.html"
        fields = (
            "batch_id",
            "batch_date",
            "model",
            "info_type",
            "cik",
            "company_name",
            "date_filed",
            "cost",
            "responses",
            "accession_number",
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
        if operator == ">":
            return queryset.filter(num_responses__gt=value)
        elif operator == ">=":
            return queryset.filter(num_responses__gte=value)
        elif operator == "<":
            return queryset.filter(num_responses__lt=value)
        elif operator == "<=":
            return queryset.filter(num_responses__lte=value)
        elif operator == "=":
            return queryset.filter(num_responses=value)
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
        elif len(search_term) == 3 and search_term.isalpha():
            queryset = queryset.filter(Q(batch_id__endswith=search_term))
        else:
            queryset = queryset.filter(Q(company_name__icontains=search_term))

        return queryset.order_by(*sort_order)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["q"] = self.request.GET.get("q", "")
        # Make request available to table for rendering links
        if "table" in context:
            context["table"].request = self.request
        return context


def readiness_check(request):
    return JsonResponse({"status": "ok"})


def health_check(request):
    return JsonResponse({"status": "ok"})


class FilingDetailView(LoginRequiredMixin, View):
    def get(self, request, filing_id):
        from urllib.parse import unquote

        filing = get_object_or_404(Filing, id=filing_id)

        # Get back URL from query parameters, default to listing page
        back_url = request.GET.get("back_url", "/")
        if back_url:
            back_url = unquote(back_url)

        context = {
            "filing": filing,
            "chunks": filing.chunks or [],
            "texts": json.dumps(filing.texts or []),
            "responses": json.dumps(filing.responses or []),
            "citation_positions": json.dumps(filing.citation_positions or []),
            "back_url": back_url,
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
