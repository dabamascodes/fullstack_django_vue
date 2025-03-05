from rest_framework.views import APIView
from django.http.response import JsonResponse
from django.http import Http404
from http import HTTPStatus
from django.contrib.auth.models import User

from .models import *

# Create your views here.

class Clase1(APIView):
    
    def post(self, request):
        if request.data.get("nombre")==None or not request.data.get("nombre"):
            return JsonResponse({"estado":"error", "mensaje":"El campo nombre es obligatorio"}, status=HTTPStatus.BAD_REQUEST)
        if request.data.get("correo")==None or not request.data.get("correo"):
            return JsonResponse({"estado":"error", "mensaje":"El campo correo es obligatorio"}, status=HTTPStatus.BAD_REQUEST)
        if request.data.get("password")==None or not request.data.get("password"):
            return JsonResponse({"estado":"error", "mensaje":"El campo password es obligatorio"}, status=HTTPStatus.BAD_REQUEST)
        
        
        if User.objects.filter(email=request.data["correo"]).exists():
            return JsonResponse({"estado":"error", "mensaje":f"El correo {request.data["correo"]} no está disponible"}, status=HTTPStatus.BAD_REQUEST)
        