from django.db import models
from root.models import Agents

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Special_services(models.Model):
    service = models.CharField(max_length=250)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.service

class Services(models.Model):
    title = models.CharField(max_length=200)
    creator = models.ForeignKey(Agents, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="services", default="default.jpg")
    content = models.TextField()
    specials = models.ManyToManyField(Special_services)
    description = models.TextField()
    category = models.ManyToManyField(Category)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    catalog_file = models.TextField(max_length=250)
    catalog_doc = models.TextField(max_length=250)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    def truncate_chars(self):
        return self.content[:20]
    

class Comments(models.Model):
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    message = models.TextField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.service.title
