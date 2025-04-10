from django.urls import path, include
from .views import ServiceDetails, ServicesView


app_name = "services"

urlpatterns = [
    path("", ServicesView.as_view(), name="services"),
    path(
        "category/<str:category>",
        ServicesView.as_view(),
        name="services-category",
    ),
    path(
        "creator/<str:name>",
        ServicesView.as_view(),
        name="service-with-creator",
    ),
    path(
        "detail/<int:pk>", ServiceDetails.as_view(), name="services-detail"
    ),
    path("api/v1/", include("services.api.v1.urls")),
]
