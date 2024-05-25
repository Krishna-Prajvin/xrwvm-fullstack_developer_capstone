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
@csrf_exempt
def registration(request):
    context = {}

    data = json.loads(request.body)
    username = data['userName']
    password = data['password']
    first_name = data['firstName']
    last_name = data['lastName']
    email = data['email']
    username_exist = False
    email_exist = False
    try:
        # Check if user already exists
        User.objects.get(username=username)
        username_exist = True
    except:
        # If not, simply log this is a new user
        logger.debug("{} is new user".format(username))

    # If it is a new user
    if not username_exist:
        # Create user in auth_user table
        user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,password=password, email=email)
        # Login the user and redirect to list page
        login(request, user)
        data = {"userName":username,"status":"Authenticated"}
        return JsonResponse(data)
    else :
        data = {"userName":username,"error":"Already Registered"}
        return JsonResponse(data)