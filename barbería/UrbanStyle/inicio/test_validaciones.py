#primer prueba automatizada
#----validaciones.py
import unittest
from datetime import date, time, timedelta
from django.conf import settings

if not settings.configured:
    settings.configure(USE_I18N=False)

from inicio.serializers import ReservaSerializer

from inicio.validaciones import (
    validar_fecha_reserva,
    validar_horario_reserva,
    validar_duracion_reserva,
)
class TestValidaciones(unittest.TestCase):
    def test_fecha_pasada(self):
        ayer = date.today() - timedelta(days=1)
        self.assertFalse(validar_fecha_reserva(ayer))

    def test_fecha_actual(self):
        self.assertTrue(validar_fecha_reserva(date.today()))

    def test_fecha_futura(self):
        manana = date.today() + timedelta(days=1)
        self.assertTrue(validar_fecha_reserva(manana))

    def test_horario_correcto(self):
        self.assertTrue(
            validar_horario_reserva(time(10), time(11))
        )

    def test_horario_invertido(self):
        self.assertFalse(
            validar_horario_reserva(time(16), time(15))
        )

    def test_horario_igual(self):
        self.assertFalse(
            validar_horario_reserva(time(12), time(12))
        )

    def test_duracion_correcta(self):
        self.assertTrue(
            validar_duracion_reserva(time(10), time(11))
        )

    def test_duracion_insuficiente(self):
        self.assertFalse(
            validar_duracion_reserva(time(10), time(10, 30))
        )

    def test_duracion_personalizada(self):
        self.assertTrue(
            validar_duracion_reserva(time(10), time(10, 30), 30)
        )
#final testeo de validaciones.py

#-----testeo seriallizers.py
class TestReservaSerializer(unittest.TestCase):
    def test_reserva_correcta(self):
        datos = {
            "fecha_reserva":(date.today() + timedelta(days=1)).isoformat(),
            "hora_inicio": "8:00",
            "hora_fin": "9:00",
        }
        reserva = ReservaSerializer(data=datos)
        self.assertTrue(reserva.is_valid())
    def test_fecha_incorrecta(self):
        datos={
            "fecha_reserva":(date.today()-timedelta(days=1)).isoformat(),
            "hora_inicio": "8:00",
            "hora_fin": "9:00"
        }
        reserva = ReservaSerializer(data=datos)
        self.assertFalse(reserva.is_valid())

    def test_horario_incorrecto(self):
        datos={
            "fecha_reserva":(date.today()+timedelta(days=1)).isoformat(),
            "hora_inicio": "14:00",
            "hora_fin": "13:00"
        }
        reserva = ReservaSerializer(data=datos)
        self.assertFalse(reserva.is_valid())
    def test_duracion_incorrecta(self):
        datos = {
            "fecha_reserva": (date.today() + timedelta(days=1)).isoformat(),
            "hora_inicio": "11:00",
            "hora_fin": "11:30"
        }
        reserva = ReservaSerializer(data=datos)
        self.assertFalse(reserva.is_valid())
    def test_formato_fecha_incorrecto(self):
        datos = {
            "fecha_reserva": "hola",
            "hora_inicio": "10:00",
            "hora_fin": "11:00"
        }
        reserva = ReservaSerializer(data=datos)
        self.assertFalse(reserva.is_valid())


if __name__ == "__main__":
    unittest.main()

