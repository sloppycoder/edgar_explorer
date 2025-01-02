# dwitter/urls.py

from django.urls import path

from trustee import views

app_name = "trustee"

urlpatterns = [
    path("healthz/", views.health_check, name="health_check"),
    path("readyz/", views.readiness_check, name="readiness_check"),
    path("", views.listing, name="listing"),
]
