from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    id_code = models.CharField(max_length=10, unique=True)
    phone = models.CharField(max_length=15, unique=True)
    image = models.ImageField(upload_to="user", default="default.jpg")

    def __str__(self):
        return self.username
