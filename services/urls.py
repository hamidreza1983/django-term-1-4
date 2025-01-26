from django.urls import path
from .views import ServicesView, ServiceDetails


app_name = "services"

urlpatterns = [
    path("", ServicesView.as_view(), name="services"),
    path("category/<str:category>", ServicesView.as_view(), name="services-category"),
    path("creator/<str:name>", ServicesView.as_view(), name="service-with-creator"),
    path("detail/<int:pk>", ServiceDetails.as_view() , name="services-detail"),

]