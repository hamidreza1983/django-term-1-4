from django.urls import path
from .views import home, contactus, aboutus

urlpatterns = [
    path("", home),
    path("contact", contactus),
    path("about", aboutus),
]
