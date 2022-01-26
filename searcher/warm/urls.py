from django.urls import path

from .views import *


urlpatterns = [
    path("heatmap/<slug:slug>/", heatmap, name="heatmap"),
    path("histogram/<slug:slug>/", histogram_page, name="histogram"),
]
