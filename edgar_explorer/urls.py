# dwitter/urls.py

from django.urls import path

from . import views
from .views import FilingDetailView, LoadNewDataView

urlpatterns = [
    path("", views.FilingsListView.as_view(), name="listing"),
    path("filing/<int:filing_id>/", FilingDetailView.as_view(), name="filing_detail"),
    path("load/", LoadNewDataView.as_view(), name="load_new"),
    # below are probes for K8S
    path("healthz/", views.health_check, name="health_check"),
    path("readyz/", views.readiness_check, name="readiness_check"),
]
