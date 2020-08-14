from django.urls import path

from . import views
urlpatterns = [
    path('', views.sign_up_r, name="sign_up_r"),
    path('Sign_up', views.sign_up_R, name="sign_up_R"),
    path('log_in', views.log_in_r, name="log_in_r"),
    path('Log_In', views.log_in_R, name="log_in_R")
]
