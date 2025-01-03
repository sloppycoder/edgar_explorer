import django_tables2 as tables
from django.db.models import Q
from django.http import JsonResponse
from django_tables2 import SingleTableView

from .models import Filing

PAGE_SIZE = 15


class TruncatedTextColumn(tables.Column):
    def render(self, value):
        return value[:20] + "..." if len(value) > 20 else value


class FilingsTable(tables.Table):
    company_name = TruncatedTextColumn(verbose_name="Company Name")

    class Meta:
        model = Filing
        template_name = "django_tables2/bootstrap5.html"
        fields = ("cik", "company_name", "date_filed", "accession_number")
        attrs = {"class": "table table-striped"}
        orderable = False


class FilingsListView(SingleTableView):
    model = Filing
    table_class = FilingsTable
    template_name = "filings_list.html"
    paginate_by = PAGE_SIZE

    def get_queryset(self):
        queryset = super().get_queryset()

        search_term = self.request.GET.get("q")
        if not search_term or len(search_term) < 4:
            return queryset.none()

        if search_term.isdigit():
            queryset = queryset.filter(
                Q(cik__icontains=search_term),
            ).order_by("-date_filed")
        elif len(search_term) == 20:
            queryset = queryset.filter(
                Q(accession_number=search_term),
            ).order_by("-date_filed")
        else:
            queryset = queryset.filter(
                Q(company_name__icontains=search_term),
            ).order_by("-date_filed")

        return queryset


def readiness_check(request):
    return JsonResponse({"status": "ok"})


def health_check(request):
    return JsonResponse({"status": "ok"})
