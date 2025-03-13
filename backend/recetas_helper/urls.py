from django.urls import path
from .views import *

urlpatterns = [
    path('recetas-h', Clase1.as_view()),
]
