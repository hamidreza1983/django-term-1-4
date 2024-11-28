from django.db import models
from root.models import Agents

# Create your models here.

class Type(models.Model):
    title  = models.CharField(max_length=150)
    def __str__(self):
        return self.title

class Method(models.Model):
    title  = models.CharField(max_length=150)

    def __str__(self):
        return self.title

class Properties(models.Model):
    image1 = models.ImageField(upload_to="property", default="default.jpg")
    image2 = models.ImageField(upload_to="property", default="default.jpg")
    image3 = models.ImageField(upload_to="property", default="default.jpg")
    title = models.CharField(max_length=150)
    content = models.TextField()
    agent = models.ForeignKey(Agents, on_delete=models.CASCADE)
    property_id = models.IntegerField(unique=True)
    location = models.CharField(max_length=150)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    method = models.ForeignKey(Method, on_delete=models.CASCADE)
    area = models.FloatField()
    beds = models.IntegerField()
    baths = models.IntegerField()
    garage = models.IntegerField()
    price = models.FloatField()
    floor = models.ImageField(upload_to="property", default="default.jpg")
    video = models.TextField()
    map = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return str(self.property_id)