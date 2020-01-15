from django.urls import path
from .views import index, get_data, ChartData, ticket_class_view_2


urlpatterns = [
    path("", ticket_class_view_2),
    path("data/", get_data),
    path("api/chart/data/", ChartData.as_view()),
]