from django.http import JsonResponse
from django.shortcuts import render


def listing(request):
    return render(request, "base.html")


def readiness_check(request):
    return JsonResponse({"status": "ok"})


def health_check(request):
    return JsonResponse({"status": "ok"})
