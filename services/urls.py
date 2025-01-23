from django.urls import path
from .views import services_detail, ServicesView


app_name = "services"

urlpatterns = [
    path("", ServicesView.as_view(), name="services"),
    path("category/<str:category>", ServicesView.as_view(), name="services-category"),
    path("creator/<str:name>", ServicesView.as_view(), name="service-with-creator"),
    path("detail/<int:id>", services_detail, name="services-detail"),

]