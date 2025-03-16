from rest_framework.views import APIView
from django.http.response import JsonResponse
from http import HTTPStatus
from django.http import Http404
from django.contrib.auth.models import User

from seguridad.decorators import logueado
from recetas.serializers import *
from recetas.models import *

# Create your views here.

# class Clase1(APIView):
    
#     def get(self, request):
#         pass
    
    
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