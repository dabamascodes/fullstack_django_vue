from rest_framework.views import APIView
from django.http.response import JsonResponse
from django.http import Http404
from http import HTTPStatus

from .models import *

# Create your views here.

class Clase1(APIView):
    
    def post(self, request):
        pass