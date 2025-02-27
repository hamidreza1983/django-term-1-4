from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from services.models import Services, Comments
from .serializer import ServiceSerializer, CommentSerializer
from rest_framework import status
from django.shortcuts import  get_object_or_404
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from .permissions import IsAdminOrReadOnly


@api_view(["GET", "POST"])
@permission_classes([IsAdminOrReadOnly])
def all_services(request):
    if request.method == "GET":
        services = Services.objects.all()
        serilize = ServiceSerializer(services, many=True)
        return Response (serilize.data, status=status.HTTP_200_OK)
    
    elif request.method == "POST":
            serilize = ServiceSerializer(data=request.data)
            if serilize.is_valid():
                serilize.save()
                return Response (serilize.data, status=status.HTTP_201_CREATED)
            else:
                return Response (serilize.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", "DELETE", "PATCH"])
def single_services (request, id):
        services = get_object_or_404(Services, id=id)
        if request.method == "GET":
            serialize = ServiceSerializer(services)
            return Response (serialize.data, status=status.HTTP_200_OK)
        elif request.method == "PUT":
             serialize = ServiceSerializer(services, data=request.data)
             serialize.is_valid(raise_exception=True)
             #if serialize.is_valid():
             serialize.save()
             return Response (serialize.data, status=status.HTTP_202_ACCEPTED)
        elif request.method == "PATCH":
             serialize = ServiceSerializer(services, data=request.data)
             serialize.is_valid(raise_exception=True)
             #if serialize.is_valid():
             serialize.save()
             return Response (serialize.data, status=status.HTTP_202_ACCEPTED)
        elif request.method == "DELETE":
             services.delete()
             return Response ({"message" : "object deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticatedOrReadOnly])
def all_comments(request):
    if request.method == "GET":
        comments = Comments.objects.all()
        serilize = CommentSerializer(comments, many=True)
        return Response (serilize.data, status=status.HTTP_200_OK)
    
    elif request.method == "POST":
        serilize = CommentSerializer(data=request.data)
        if serilize.is_valid():
            serilize.save()
            return Response (serilize.data, status=status.HTTP_201_CREATED)
        else:
            return Response (serilize.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "DELETE", "PATCH"])
@permission_classes([IsAuthenticatedOrReadOnly])
def single_comment (request, id):
        comment = get_object_or_404(Comments, id=id)
        if request.method == "GET":
            serialize = CommentSerializer(comment)
            return Response (serialize.data, status=status.HTTP_200_OK)
        elif request.method == "PATCH":
             if request.user.id == comment.name.id :
                serialize = CommentSerializer(comment, data=request.data)
                serialize.is_valid(raise_exception=True)
                #if serialize.is_valid():
                serialize.save()
                return Response (serialize.data, status=status.HTTP_202_ACCEPTED)
             else:
                 return Response ({"message" : "this object is not for you"}, status=status.HTTP_400_BAD_REQUEST)
                              
        elif request.method == "DELETE":
             if request.user.id == comment.name.id :
                comment.delete()
                return Response ({"message" : "object deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
             else:
                 return Response ({"message" : "this object is not for you"}, status=status.HTTP_400_BAD_REQUEST)

