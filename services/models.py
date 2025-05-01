from django.db import models
from root.models import Agents
from accounts.models import User

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
    content = models.TextField(default="text default")
    specials = models.ManyToManyField(Special_services, null=True, blank=True)
    description = models.TextField(default="text description")
    category = models.ManyToManyField(Category)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    catalog_file = models.TextField(max_length=250, default="text catalog file")
    catalog_doc = models.TextField(max_length=250, default="text catalog doc")
    status = models.BooleanField(default=False)
    price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def truncate_chars(self):
        return self.content[:20]


class Comments(models.Model):
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.service.title
None