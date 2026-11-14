from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("artículos/", views.articulos, name="artículos"),
    path("personal/", views.personal, name="personal"),
    path("reservas/", views.reservas, name="reservas"),
    ]