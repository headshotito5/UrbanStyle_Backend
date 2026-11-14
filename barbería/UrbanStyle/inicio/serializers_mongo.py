
from django_mongodb_extensions.rest_framework import MongoModelSerializer
from .models import Barbero, Producto, Servicio, Reserva
from rest_framework import serializers


class BarberoSerializer(MongoModelSerializer):
    class Meta:
        model = Barbero
        fields = "__all__"
class ProductoSerializer(MongoModelSerializer):
    class Meta:
        model = Producto
        fields = "__all__"
    def validate_precio(self, value):
        if value < 0:
            raise serializers.ValidationError("precio invalido")
        return value

    def validate_stock(self, value):
        if value < 0:
            raise serializers.ValidationError("stock invalido")
        return value
    
class ServicioSerializer(MongoModelSerializer):
    class Meta:
        model = Servicio
        fields = "__all__"
    def validate_precio(self, value):
        if value < 0:
            raise serializers.ValidationError("precio invalido")
        return value

    def validate_duracion(self, value):
        if value <= 0:
            raise serializers.ValidationError("duracion invalida")
        return value

class ReservaMongoSerializer(MongoModelSerializer):
    class Meta:
        model = Reserva
        fields = "__all__"
