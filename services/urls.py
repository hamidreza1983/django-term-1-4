from django.urls import path, include
from .views import ServiceDetails, services


app_name = "services"

urlpatterns = [
    path("", services, name="services"),
    path("category/<str:category>", services, name="services-category"),
    path("creator/<str:name>", services, name="service-with-creator"),
    path("detail/<int:pk>", ServiceDetails.as_view() , name="services-detail"),
    path("api/v1/", include("services.api.v1.urls"))

]