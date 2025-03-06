from rest_framework.views import APIView
from django.http.response import JsonResponse
from django.http import Http404
from http import HTTPStatus
from django.contrib.auth.models import User
import uuid
import os
from dotenv import load_dotenv

from .models import *
from utilidades import utilidades

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
        
        
        token = uuid.uuid4()
        url = f"{os.getenv("BASE_URL")}api/v1/seguridad/verificacion/{token}"
        try:
            # Sólo para User de Django Admin
            u=User.objects.create_user(
                username=request.data["correo"], 
                password=request.data["password"],
                email=request.data["correo"],
                first_name=request.data["nombre"],
                last_name="",
                is_active = 0
            )
            UsersMetadata.objects.create(token=token, user_id=u.id)
            
            html=f"""
            <h3>Verificación de cuenta</h3>
            Hola {request.data["nombre"]} te haz registrado exitosamente. Para activar tu cuenta haz click en el siguiente enlace:<br/>
            <a href="{url}">{url}</a> 
            <br/>
            o copia y pega la siguiente URL en tu navegador favorito:
            <br/>
            {url}
            """
            utilidades.sendMail(html, "Verificación", request.data["correo"])
            
        except Exception as e:
            return JsonResponse({"estado":"error", "mensaje":"Ocurrió un error inesperado"}, status=HTTPStatus.BAD_REQUEST)
        
        return JsonResponse({"estado":"ok", "mensaje":"Se crea el registro exitosamente"}, status=HTTPStatus.CREATED)