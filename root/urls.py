from django.urls import path
from .views import (
    contactus,
    AgentsView,
    HomeView,
    AboutView,
    GoogleView,
    test,
)


app_name = "root"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("contact", contactus, name="contact"),
    path("about", AboutView.as_view(), name="about"),
    path("agent", AgentsView.as_view(), name="agent"),
    path("google", GoogleView.as_view(), name="google"),
    path("api", test),
]
