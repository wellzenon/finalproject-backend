import json
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.views.decorators.http import require_POST
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser as User


def get_csrf(request):
    response = JsonResponse({"info": "CSRF cookie succesfully set"})
    response["X-CSRFToken"] = get_token(request)
    return response

def logoutView(request):
    logout(request)
    return JsonResponse({"info": "User logged out"})

@require_POST
def loginView(request):
    data = json.loads(request.body)
    username = data.get("username")
    password = data.get("password")

    if None in [username, password]:
        return JsonResponse({"info": "Email or User name and Password required"}, status=400)
    
    if not (
        User.objects.filter(email=username).exists() 
        or User.objects.filter(username=username).exists()
    ):
        return JsonResponse({"info": "Invalid credentials"}, status=400)
    
    if not User.objects.filter(email=username).exists():
        username = User.objects.get(username=username).email

    user = authenticate(username=username, password=password)

    if user is None:
        return JsonResponse({"info": "User does not exist or is innactive"}, status=400)
    
    login(request, user)
    return JsonResponse({"username": user.username})

@require_POST
def signUpView(request):
    data = json.loads(request.body)
    username = data.get("username")
    email = data.get("email")
    birthday = data.get("birthday")
    password = data.get("password")
    confirm = data.get("confirm")

    if None in [username, email, password, birthday]:
        return JsonResponse({"info": "Email, User name, Password and Birthday required"})
    
    if password != confirm:
        return JsonResponse({"info": "Passwords must match"})

    if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
        return JsonResponse({"info": "User or email already taken"}, status=400)
    
    user = User(username=username, email=email, birthday=birthday, is_active=True)
    user.set_password(password)
    user.save()
    
    login(request, user)
    return JsonResponse({"username": user.username})