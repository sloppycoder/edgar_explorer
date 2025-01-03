from django.contrib import admin

from .models import Filing


@admin.register(Filing)
class FilingAdmin(admin.ModelAdmin):
    list_display = (
        "cik",
        "company_name",
        "form_type",
        "accession_number",
        "date_filed",
    )

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return False
