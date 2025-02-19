from django.urls import path
# from home.views import *
from .views import *

urlpatterns = [
    path('', home_inicio)
]

