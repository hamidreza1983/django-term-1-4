from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Ability(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Agents(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ability = models.ForeignKey(Ability, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="agent", default="default.jpg")
    twitter = models.CharField(max_length=220)
    instagram = models.CharField(max_length=220)
    facebook = models.CharField(max_length=220)
    linkedin = models.CharField(max_length=220)
    status = models.BooleanField(default=False)


    def __str__(self):
        return self.user.first_name
