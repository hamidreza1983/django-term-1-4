from django.urls import path, include
from .views import (
    contactus,
    AgentsView,
    HomeView,
    AboutView,
    GoogleView,
    contactusapi
)


app_name = "root"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("contact", contactus, name="contact"),
    path("contactus", contactusapi, name="contactapi"),
    path("about", AboutView.as_view(), name="about"),
    path("agent", AgentsView.as_view(), name="agent"),
    path("google", GoogleView.as_view(), name="google"),
    path("api/v1/", include("root.api.v1.urls")),
]
