from django.urls import path
from .views import services


app_name = "services"

urlpatterns = [
    path("", services, name="services"),

]