from django.urls import path
from .views import *


app_name = "api-services"

urlpatterns = [
    path("services", all_services, name="all_services"),
    path("service-detail/<int:id>", single_services, name="single_services"),
    path("comments", all_comments, name="all_comments"),
    path("comment-detail/<int:id>", single_comment, name="single_comment"),
]
