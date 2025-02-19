from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_inicio(request):
    # Aqui podriasmos retornar un HTML, pero vamos a usar Django solamente como backend.
    return HttpResponse("<h1>Hola mundo desde Django 5.1</h1>")
