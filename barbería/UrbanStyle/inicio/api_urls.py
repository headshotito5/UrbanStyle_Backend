from rest_framework.routers import DefaultRouter
from.import views
from django.urls import path, include

router = DefaultRouter()
router.register("servicios", views.ServicioViewSet, basename="servicio")
router.register("barberos", views.BarberoViewSet, basename="barbero")
router.register("reservas", views.ReservaViewSet, basename="reserva")
router.register("productos", views.ProductoViewSet, basename="producto")
urlpatterns = [
    path("", include(router.urls)),
]