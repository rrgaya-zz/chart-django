from django.urls import path
from .views import index, homechart, get_data

urlpatterns = [
    path("", index),
    path("charts/", homechart),
    path("data/", get_data),
]