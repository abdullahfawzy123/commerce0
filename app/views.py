from django.shortcuts import render
from .models import User
# Create your views here.

def sign_up_r(request):
    return render(request, "signup.html")


def log_in_r(request):
    return render(request, "login.html")


def sign_up_R(request):
    return render(request, "signup.html")


def log_in_R(request):
    return render(request, "login.html")
