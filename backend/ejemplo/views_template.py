from rest_framework.views import APIView
from django.http import HttpResponse

# Create your views here.
class Class_Ejemplo(APIView):
    
    def get(self, request):
        return HttpResponse("Método GET")
    

    def post(self, request):
        return HttpResponse("Método POST")
    
    
class Class_EjemploParametros(APIView):
    
    def get(self, request, id):
        return HttpResponse(f"Método GET | parámetro={id}")
    
    
    def put(self, request, id):
        return HttpResponse(f"Método PUT | parámetro={id}")
    
    
    def delete(self, request, id):
        return HttpResponse(f"Método DELETE | parámetro={id}")
