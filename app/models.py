from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    password = models.IntegerField(max_length=32)
