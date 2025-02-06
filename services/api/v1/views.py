from rest_framework.response import Response
from rest_framework.decorators import api_view
from services.models import Services
from .serializer import ServiceSerializer
from rest_framework import status



@api_view(["GET", "POST"])
def all_services(request):
    if request.method == "GET":
        services = Services.objects.all()
        serilize = ServiceSerializer(services, many=True)
        return Response (serilize.data, status=status.HTTP_200_OK)
    

@api_view(["GET"])
def single_services (request, id):
    try :
        services = Services.objects.get(id=id)
        serilize = ServiceSerializer(services)
        return Response (serilize.data, status=status.HTTP_200_OK)
    except Services.DoesNotExist :
        return Response ({"message" : "object not found",}, status=status.HTTP_404_NOT_FOUND)