# dwitter/urls.py

from django.urls import path

from . import views

urlpatterns = [
    path("", views.FilingsListView.as_view(), name="listing"),
    path("load/", views.load_new_data, name="load_new"),
    # below are probes for K8S
    path("healthz/", views.health_check, name="health_check"),
    path("readyz/", views.readiness_check, name="readiness_check"),
]
