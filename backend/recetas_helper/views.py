from rest_framework.views import APIView
from django.http.response import JsonResponse
from http import HTTPStatus
from django.http import Http404
from django.contrib.auth.models import User


from dotenv import load_dotenv
import os
from datetime import datetime
from django.core.files.storage import FileSystemStorage


from seguridad.decorators import logueado
from recetas.serializers import *
from recetas.models import *

# Create your views here.

class Clase1(APIView):   
     
    def post(self, request):
        if request.data.get("id")==None or not request.data.get("id"):
            return JsonResponse({"estado":"error", "mensaje":"El campo id es obligatorio"}, status=HTTPStatus.BAD_REQUEST)
        
        try:
            existe=Receta.objects.filter(pk=request.data["id"]).get()
            anterior = existe.foto
        except Receta.DoesNotExist:
            return JsonResponse({"estado":"error", "mensaje":"La receta informada no existe en la base de datos"}, status=HTTPStatus.BAD_REQUEST)
        
        
        fs = FileSystemStorage()
        try:
            foto = f"{datetime.timestamp(datetime.now())}{os.path.splitext(str(request.FILES['foto']))[1]}"
        except Exception as e:
            return JsonResponse({"estado":"error", "mensaje":f"Debe adjuntar una foto en el campo foto"}, status=HTTPStatus.BAD_REQUEST) 
        
        if request.FILES["foto"].content_type=="image/jpeg" or request.FILES["foto"].content_type=="image/png":  
            
            try:
                fs.save(f"recetas/{foto}", request.FILES['foto'])
                fs.url( request.FILES['foto'])
            except Exception as e:
                return JsonResponse({"estado":"error", "mensaje":f"Se produjo un error al intentar subir el archivo"}, status=HTTPStatus.BAD_REQUEST)  
            
            try:
                Receta.objects.filter(id=request.data["id"]).update(foto=foto)
                os.remove(f"./uploads/recetas/{anterior}")
                
                return JsonResponse({"estado":"ok", "mensaje":"Se modifica el registro exitosamente"}, status=HTTPStatus.OK)  
            except Exception as e:
                return JsonResponse({"estado":"error", "mensaje":"Ocurrió un error inesperado"}, status=HTTPStatus.BAD_REQUEST)  
            
        else:
            return JsonResponse({"estado":"error", "mensaje":"La foto sólo puede ser PNG y JPG"}, status=HTTPStatus.BAD_REQUEST)
    
    
class Clase4(APIView):
    

    @logueado()    
    def get(self, request, id):
        try:
            existe = User.objects.filter(pk=id).get()
        except User.DoesNotExist:
            return JsonResponse({"estado" : "error", "mensaje" : "Ocurrió un error inesperado" }, status=HTTPStatus.BAD_REQUEST)

        
        data = Receta.objects.filter(user_id=id).order_by('-id').all()
        datos_json=RecetaSerializer(data, many=True)
        return JsonResponse({"data":datos_json.data}, status=HTTPStatus.OK)