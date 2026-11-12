#python -m pip install djangorestframework
from rest_framework import serializers

from .validaciones import (
    validar_fecha_reserva,
    validar_horario_reserva,
    validar_duracion_reserva
)
class ReservaSerializer(serializers.Serializer):
    fecha_reserva = serializers.DateField()
    hora_inicio = serializers.TimeField()
    hora_fin = serializers.TimeField()

    def validate(self, data):
        fecha = data["fecha_reserva"]
        inicio = data["hora_inicio"]
        fin = data["hora_fin"]

        if validar_fecha_reserva(fecha) == False:
            raise serializers.ValidationError("fecha invALIDA")

        if validar_horario_reserva(inicio, fin) == False:
            raise serializers.ValidationError("horario invalido")

        if validar_duracion_reserva(inicio, fin) == False:
            raise serializers.ValidationError("duracion invalida")

        return data
