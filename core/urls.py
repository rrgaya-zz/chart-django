from django.urls import path
from .views import index, get_data, ChartData


urlpatterns = [
    path("", index),
    path("data/", get_data),
    path("api/chart/data/", ChartData.as_view()),
]