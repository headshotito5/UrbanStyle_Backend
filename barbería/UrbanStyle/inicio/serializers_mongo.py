
from django_mongodb_extensions.rest_framework import MongoModelSerializer
from .models import Barbero, Producto, Servicio, Reserva


class BarberoSerializer(MongoModelSerializer):
    class Meta:
        model = Barbero
        fields = "__all__"
class ProductoSerializer(MongoModelSerializer):
    class Meta:
        model = Producto
        fields = "__all__"
class ServicioSerializer(MongoModelSerializer):
    class Meta:
        model = Servicio
        fields = "__all__"
class ReservaMongoSerializer(MongoModelSerializer):
    class Meta:
        model = Reserva
        fields = "__all__"
