from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import logout
from django.contrib import messages
from datetime import datetime
from django.http import JsonResponse
from django.contrib.auth import login, authenticate
import logging
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.generic.base import View
from.populate import initiate
import hashlib

# Get an instance of a logger
logger = logging.getLogger(__name__)

# Decorator to disable CSRF protection for this view
@csrf_exempt
def login_user(request):
    data = json.loads(request.body)
    username = data['userName']
    password = data['password']
    user = authenticate(username=username, password=password)
    data = {"userName": username}
    if user is not None:
        login(request, user)
        data = {"userName": username, "status": "Authenticated"}
    return JsonResponse(data)

@csrf_exempt
def logout_request(request):
    logout(request)
    data = {"userName": ""}
    return JsonResponse(data)

@csrf_exempt
def register_view(request):
    context = {}
    data = json.loads(request.body)
    username = data['userName']
    password = data['password']
    first_name = data['firstName']
    last_name = data['lastName']
    email = data['email']

    # Validación básica de entrada
    if not all([username, password, first_name, last_name, email]):
        return JsonResponse({"error": "Todos los campos son obligatorios"}, status=400)

    # Verificar si el usuario ya existe
    if User.objects.filter(username=username).exists():
        return JsonResponse({"error": "El usuario ya existe"}, status=400)

    try:
        # Crear usuario
        user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, password=password, email=email)
        login(request, user)
        return JsonResponse({"message": "Usuario registrado exitosamente"})
    except IntegrityError as e:
        logger.error(f"Error al registrar usuario: {e}")
        return JsonResponse({"error": "Hubo un error al registrar el usuario"}, status=500)