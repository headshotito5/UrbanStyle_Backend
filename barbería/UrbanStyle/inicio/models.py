from django.db import models
from django.conf import settings
from django_mongodb_backend.fields import ArrayField


class Barbero(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    horario = ArrayField(models.CharField(max_length=100), null=True, blank=True)

    class Meta:
            db_table = "barbero"
            managed = False
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    marca = models.TextField(blank=True)
    nombre = models.CharField(max_length=100)
    categoria = models.TextField(blank=True)
    precio = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)

    class Meta:
        db_table = "producto"
        managed = False

    def __str__(self):
        return self.nombre, self.precio

class Reserva(models.Model):
    nombre_cliente = models.CharField(max_length=100)
    apellido_cliente = models.CharField(max_length=100)
    horario = ArrayField(models.CharField(max_length=100), null=True, blank=True)
    id_cliente = models.TextField(blank=False)
    barbero = models.CharField(max_length=100)

    class Meta:
        db_table = "reserva"
        managed = False

    def __str__(self):
        return self.nombre_cliente, self.horario

class Servicio(models.Model):
    servicio = models.CharField(max_length=100)
    duracion = models.IntegerField(default=0)
    precio = models.IntegerField(default=0)

    class Meta:
        db_table = "servicio"
        managed = False

    def __str__(self):
        return self.servicio