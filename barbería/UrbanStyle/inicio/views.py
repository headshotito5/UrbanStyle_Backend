from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status 

def inicio(request): 
    contexto = {
    "titulo": "Barbería Urban Style",        
    "mensaje": "Bienvenidos al desarrollo Backend",        
    "asignatura": "Desarrollo de Aplicaciones Web"    
    }    
    return render(request, "inicio/inicio.html", contexto)
