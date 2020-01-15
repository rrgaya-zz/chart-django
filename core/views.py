from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import Passenger
from django.db.models import Count, Q

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

User = get_user_model()


def index(request):
    return render(request, "core/index.html", {"customers": 25})


def get_data(request, *args, **kwargs):
    data = {
        "sales": 100,
        "customers": 10,
    }
    return JsonResponse(data)


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        qs_count = User.objects.all().count()
        labels = ["User", "Red", "Blue", "Yellow", "Green", "Purple", "Orange"]
        default_items = [qs_count, 2, 5, 2, 1, 3]
        data = {
            "labels": labels,
            "default": default_items,
            "sales": 100,
            "customers": 10,
            "users": User.objects.all().count(),
        }
        return Response(data)


def ticket_class_view(request):
    dataset = (
        Passenger.objects.values("ticket_class")
        .annotate(
            survived_count=Count("ticket_class", filter=Q(survived=True)),
            not_survived=Count("ticket_class", filter=Q(survived=False)),
        )
        .order_by("ticket_class")
    )
    return render(request, "ticket_class.html", {"dataset": dataset})