from django.shortcuts import render

# Create your views here.

def sign_up_r(request):
    return render(request, "signup.html")


def log_in_r(request):
    return render(request, "login.html")
