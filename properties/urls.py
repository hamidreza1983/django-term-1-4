from django.urls import path
from .views import properties, property_detail


app_name = "properties"

urlpatterns = [
    path("", properties, name="properties"),
    path("detail/<int:id>", property_detail, name="property-detail"),
]