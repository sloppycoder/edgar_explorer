# dwitter/urls.py

from django.urls import path

from . import views

app_name = "trustee"

urlpatterns = [
    path("", views.FilingsListView.as_view(), name="listing"),
    # below are probes for K8S
    path("healthz/", views.health_check, name="health_check"),
    path("readyz/", views.readiness_check, name="readiness_check"),
]
