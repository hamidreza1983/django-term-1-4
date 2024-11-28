from django.urls import path
from .views import services, services_detail


app_name = "services"

urlpatterns = [
    path("", services, name="services"),
    path("category/<str:category>", services, name="services-category"),
    path("creator/<str:name>", services, name="service-with-creator"),
    path("detail/<int:id>", services_detail, name="services-detail"),

]