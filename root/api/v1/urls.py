from django.urls import path
from .views import *


app_name = "api-root"

urlpatterns = [
    path(
        "contactus/",
        ContactView.as_view({"post": "create"}),
        name="create-contact",
    ),
]