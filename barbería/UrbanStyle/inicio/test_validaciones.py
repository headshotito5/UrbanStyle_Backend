#primer prueba automatizada
#----validaciones.py
import unittest
from datetime import date, time, timedelta

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
if __name__ == "__main__":
    unittest.main()
