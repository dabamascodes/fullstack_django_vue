# Código Original -> Curso
from rest_framework.views import APIView
from .models import *
from django.http.response import JsonResponse
from http import HTTPStatus
from datetime import datetime, timezone

# Llamamos a utilidades
from utilidades import utilidades


# swagger
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Create your views here.
class Clase1(APIView):
    
    @swagger_auto_schema(
        operation_description="Endpoint para Contacto",
        responses = {
            200: "Success",
            400: "Bad request"
        },
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'nombre':openapi.Schema(type=openapi.TYPE_STRING, description="Nombre"),
                'correo':openapi.Schema(type=openapi.TYPE_STRING, description="E-Mail"),
                'telefono':openapi.Schema(type=openapi.TYPE_STRING, description="Télefono"),
                'mensaje':openapi.Schema(type=openapi.TYPE_STRING, description="Mensaje"),

            },
            required=['nombre', 'correo', 'telefono', 'mensaje']
        )
    )
    def post(self, request):
        if request.data.get("nombre")==None or not request.data['nombre']:
            return JsonResponse({"estado":"error", "mensaje":"El campo nombre es obligatorio"}, status=HTTPStatus.BAD_REQUEST)
        
        if request.data.get("correo")==None or not request.data['correo']:
            return JsonResponse({"estado":"error", "mensaje":"El campo correo es obligatorio"}, status=HTTPStatus.BAD_REQUEST)
        
        if request.data.get("telefono")==None or not request.data['telefono']:
            return JsonResponse({"estado":"error", "mensaje":"El campo telefono es obligatorio"}, status=HTTPStatus.BAD_REQUEST)
        
        if request.data.get("mensaje")==None or not request.data['mensaje']:
            return JsonResponse({"estado":"error", "mensaje":"El campo mensaje es obligatorio"}, status=HTTPStatus.BAD_REQUEST)
        
        
        try:
            Contacto.objects.create(
                nombre = request.data['nombre'],
                correo = request.data['correo'],
                telefono = request.data['telefono'],
                mensaje = request.data['mensaje'],
                fecha = datetime.now()
            )
            
            html=f"""
                <h1>Nuevo mensaje de sitio web</h1>
                <ul>
                    <li>Nombre: {request.data['nombre']}</li>
                    <li>E-Mail: {request.data['correo']}</li>
                    <li>Télefono: {request.data['telefono']}</li>
                    <li>Mensaje: {request.data['mensaje']}</li>
                </ul>
            """
            utilidades.sendMail(html, "Prueba curso", request.data['correo'])
        except Exception as e:
            return JsonResponse({"estado":"error", "mensaje":"Ocurrió un error inesperado"}, status=HTTPStatus.BAD_REQUEST)

        
        return JsonResponse({"estado":"ok", "mensaje":"Se crea el registro exitosamente"}, status=HTTPStatus.OK)





# # Código Mejorado
# from rest_framework.views import APIView
# from .models import Contacto
# from django.http.response import JsonResponse
# from http import HTTPStatus
# from datetime import datetime
# import logging
# # from django.utils import timezone

# # Llamamos a utilidades
# from utilidades import utilidades

# # Configurar logging para ver errores
# logging.basicConfig(level=logging.DEBUG)

# class Clase1(APIView):

#     def post(self, request):
#         # Validar datos requeridos
#         for campo in ["nombre", "correo", "telefono", "mensaje"]:
#             if not request.data.get(campo):
#                 return JsonResponse({"estado": "error", "mensaje": f"El campo {campo} es obligatorio"}, status=HTTPStatus.BAD_REQUEST)

#         try:
#             # Crear registro en la base de datos
#             contacto = Contacto.objects.create(
#                 nombre=request.data['nombre'],
#                 correo=request.data['correo'],
#                 telefono=request.data['telefono'],
#                 mensaje=request.data['mensaje'],
#                 fecha=datetime.now()
#                 # fecha=timezone.now()  # Asegurar fecha con zona horaria
#             )

#             # Construir HTML para el correo
#             html = f"""
#                 <h1>Nuevo mensaje de sitio web</h1>
#                 <ul>
#                     <li>Nombre: {contacto.nombre}</li>
#                     <li>E-Mail: {contacto.correo}</li>
#                     <li>Télefono: {contacto.telefono}</li>
#                     <li>Mensaje: {contacto.mensaje}</li>
#                 </ul>
#             """

#             # Intentar enviar el correo
#             utilidades.sendMail(html, "Prueba curso", contacto.correo)
            
#         except Exception as e:
#             logging.error(f"Error al guardar el contacto o enviar correo: {e}", exc_info=True)
#             return JsonResponse({"estado": "error", "mensaje": f"Ocurrió un error inesperado: {str(e)}"}, status=HTTPStatus.BAD_REQUEST)

#         return JsonResponse({"estado": "ok", "mensaje": "Se crea el registro exitosamente"}, status=HTTPStatus.OK)

