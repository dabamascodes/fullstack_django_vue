from functools import wraps
from django.http.response import JsonResponse
from django.contrib.auth.models import User
from http import HTTPStatus
from jose import jwt
from django.conf import settings
import time

def logueado():
    def metodo(func):
        @wraps(func)
        def _decorator(request, *args, **kwars):
            req = args[0]
            if not req.headers.get('Authorization') or req.headers.get('Authorization')==None:
                return JsonResponse({"estado":"error", "mensaje":"No autorizado"}, status=HTTPStatus.UNAUTHORIZED)
            header = req.headers.get('Authorization').split(" ")
            try:
                # Agregar Validación para comprobar sí el usuario está activo
                resuelto=jwt.decode(header[1], settings.SECRET_KEY, algorithms=['HS512'])  
                # Tomamos el user_id del JWT, y vamos a la tabla de auth_user a comprobar sí existe y si está activo el usuario
                # Sí NO ESTÁ ACTIVO ó NO EXISTE, devolvemos un UNAUTHORIZED
                # Como nmos damos cuenta, se puede generar el token correctamente, pero se pudiera manipular el user en la tabla y con eso se accederia
                # Es por ello que agregamos este filtro al final de la validación
                user_id = resuelto.get("id")
                user = User.objects.filter(id=user_id).first()

                if not user:
                    # print('NOT EXISTS')
                    return JsonResponse({"estado":"error", "mensaje":"No autorizado"}, status=HTTPStatus.UNAUTHORIZED)
                if not user.is_active:
                    # print('IS INACTIVE')
                    return JsonResponse({"estado":"error", "mensaje":"No autorizado"}, status=HTTPStatus.UNAUTHORIZED)
                
            except Exception as e:
                return JsonResponse({"estado":"error", "mensaje":"No autorizado"}, status=HTTPStatus.UNAUTHORIZED)
            
            if int(resuelto["exp"])>int(time.time()):
                return func(request, *args, **kwars)
            else:
                return JsonResponse({"estado":"error", "mensaje":"No autorizado"}, status=HTTPStatus.UNAUTHORIZED)

        return _decorator
    return metodo
                