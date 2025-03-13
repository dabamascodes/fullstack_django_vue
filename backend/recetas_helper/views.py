from rest_framework.views import APIView
from django.http.response import JsonResponse
from http import HTTPStatus
from django.http import Http404

# Create your views here.

class Clase1(APIView):
    
    def get(self, request):
        pass
