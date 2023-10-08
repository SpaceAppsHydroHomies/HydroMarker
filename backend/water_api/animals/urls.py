from django.urls import path
from . import views

urlpatterns = [
    path(
        "get_endangered_species_data/<str:ecosystem_name>/",
        views.get_endangered_species_data,
        name="get_endangered_species_data",
    ),
    path("get_ecosystems/", views.get_ecosystems, name="get_ecosystems"),
]
