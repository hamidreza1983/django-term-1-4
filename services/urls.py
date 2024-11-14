from django.urls import path
from .views import services, services_detail


app_name = "services"

urlpatterns = [
    path("/", services, name="services"),
    path("/detail/<int:id>", services_detail, name="services-detail"),

]