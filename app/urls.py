from django.urls import path

from . import views
urlpatterns = [
    path('', views.sign_up_r, name="sign_up_r"),
    path('log_in', views.log_in_r, name="log_in_r")
]
