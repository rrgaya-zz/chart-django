from django.shortcuts import render
from django.http import JsonResponse


def index(request):
    return render(request, "core/index.html", {})


def homechart(request):
    return render(request, "core/charts.html", {})


def get_data(request, *args, **kwargs):
    data = {
        "sales": 100,
        "customers": 10, 
    }
    return JsonResponse(data)