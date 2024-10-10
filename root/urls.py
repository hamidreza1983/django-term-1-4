from django.urls import path
from .views import home, contactus, aboutus, agent


app_name = "root"

urlpatterns = [
    path("", home, name="home"),
    path("contact", contactus, name="contact"),
    path("about", aboutus, name="about"),
    path("agent", agent, name="agent"),
]
