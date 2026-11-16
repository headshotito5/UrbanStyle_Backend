from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("articulos/", views.articulos, name="articulos"),
    path("servicios/", views.servicios, name="servicios"),
    path("personal/", views.personal, name="personal"),
    path("reservas/", views.reservas, name="reservas"),
    ]