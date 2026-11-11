#aplicale al ( python -m pip install djangorestframework ) sin parentesis bebé
from rest_framework import serializers

from .validaciones import (
    validar_fecha_reserva,
    validar_horario_reserva,
    validar_duracion_reserva
)
#hasta donde sé luego ya todo es desconocido