# server/djangoapp/views.py

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import login, authenticate, logout
from django.views.decorators.csrf import csrf_exempt
import logging
import json

# Get an instance of a logger
logger = logging.getLogger(__name__)

@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        # Get username and password from request body
        data = json.loads(request.body)
        username = data.get('userName')
        password = data.get('password')

        # Authenticate user
        user = authenticate(username=username, password=password)
        if user is not None:
            # If user is valid, login and return JSON response
            login(request, user)
            response_data = {"userName": username, "status": "Authenticated"}
        else:
            # If authentication fails, return JSON response with error
            response_data = {"status": "Failed", "error": "Invalid credentials"}

        return JsonResponse(response_data)
    else:
        return JsonResponse({"status": "Failed", "error": "Invalid request method"})

@csrf_exempt
def logout_user(request):
    if request.method == 'POST':
        # Logout the user
        username = request.user.username
        logout(request)
        # Return JSON response with the username
        return JsonResponse({"userName": username, "status": "Logged out"})
    else:
        return JsonResponse({"status": "Failed", "error": "Invalid request method"})
