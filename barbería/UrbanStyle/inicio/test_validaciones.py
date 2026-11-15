#primer prueba automatizada
#----validaciones.py
import os
import unittest
import django

from datetime import date, time, timedelta

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from inicio.serializers import ReservaSerializer
from inicio.serializers_mongo import ProductoSerializer, ServicioSerializer

from inicio.validaciones import (
    validar_fecha_reserva,
    validar_horario_reserva,
    validar_duracion_reserva
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

class TestMongoSerializers(unittest.TestCase):
    def test_producto_correcto(self):
        datos = {
            "nombre": "Cera",
            "precio": 5000,
            "stock": 10
        }
        producto = ProductoSerializer(data=datos)
        self.assertTrue(producto.is_valid())
    def test_producto_precio_incorrecto(self):
        datos = {
            "nombre": "Cera",
            "precio": -5000,
            "stock": 10
        }
        producto = ProductoSerializer(data=datos)
        self.assertFalse(producto.is_valid())
        self.assertIn("precio", producto.errors)
    def test_producto_stock_incorrecto(self):
        datos = {
            "nombre": "Cera",
            "precio": 5000,
            "stock": -10
        }
        producto = ProductoSerializer(data=datos)
        self.assertFalse(producto.is_valid())
        self.assertIn("stock", producto.errors)
    def test_servicio_correcto(self):
        datos = {
            "servicio": "Corte de cabello",
            "precio": 5000,
            "duracion": 60
        }
        servicio = ServicioSerializer(data=datos)
        self.assertTrue(servicio.is_valid())
    def test_servicio_precio_incorrecto(self):
        datos = {
            "servicio": "Corte de cabello",
            "precio": -5000,
            "duracion": 60
        }
        servicio = ServicioSerializer(data=datos)
        self.assertFalse(servicio.is_valid())
        self.assertIn("precio", servicio.errors)
    def test_servicio_duracion_incorrecta(self):
        datos = {
            "servicio": "Corte de cabello",
            "precio": 5000,
            "duracion": 0
        }
        servicio = ServicioSerializer(data=datos)
        self.assertFalse(servicio.is_valid())
        self.assertIn("duracion", servicio.errors)

if __name__ == "__main__":
    unittest.main()

