from.serializers_mongo import BarberoSerializer, ProductoSerializer, ServicioSerializer, ReservaMongoSerializer 
from django.shortcuts import render
from .models import Barbero, Producto, Servicio, Reserva 
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status 

def inicio(request): 
    contexto = {
    "titulo": "Barbería Urban Style",        
    "mensaje": "Bienvenidos al Backend de Urban Style",        
    "asignatura": "Desarrollo de Aplicaciones Web"    
    }    
    return render(request, "inicio/inicio.html", contexto)

def articulos(request):
    articulo = Producto.objects.order_by("\nnombre")
    servicio = Servicio.objects.order_by("\nnombre")
    return render(request, "inicio/articulos.html", articulo, servicio)

def personal(request):
    personal = Barbero.objects.order_by("\nnombre")
    return render(request, "inicio/personal.html", personal)

def reservas(request):
    reserva = Reserva.objects.order_by("\nnombre_cliente")
    return render(request, "inicio/reservas.html", reserva)

class ServicioViewSet(viewsets.ModelViewSet):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer

class BarberoViewSet(viewsets.ModelViewSet):
    queryset = Barbero.objects.all()
    serializer_class = BarberoSerializer

class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaMongoSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer