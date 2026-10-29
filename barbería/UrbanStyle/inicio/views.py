from django.shortcuts import render

def inicio(request): 
    contexto = {
    "titulo": "Barbería Urban Style",        
    "mensaje": "Bienvenidos al desarrollo Backend",        
    "asignatura": "Desarrollo de Aplicaciones Web"    
    }    
    return render(request, "inicio/inicio.html", contexto)
