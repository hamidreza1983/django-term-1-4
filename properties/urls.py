from django.urls import path
from .views import properties


app_name = "properties"

urlpatterns = [
    path("", properties, name="properties"),

]