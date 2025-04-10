# from rest_framework.response import Response
# from rest_framework.decorators import api_view, permission_classes
from services.models import Services, Comments
from .serializer import ServiceSerializer, CommentSerializer

# from rest_framework import status
# from django.shortcuts import  get_object_or_404
from rest_framework.permissions import (
    IsAdminUser,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
    AllowAny,
)
from .permissions import IsAdminOrReadOnly
from rest_framework.viewsets import ViewSet, ModelViewSet

# from rest_framework.views import APIView
# from rest_framework.mixins import (
#     ListModelMixin,
#     CreateModelMixin,
#     RetrieveModelMixin,
#     UpdateModelMixin,
#     DestroyModelMixin
# )
# from rest_framework.generics import (
#     GenericAPIView,
#     ListAPIView,
#     CreateAPIView,
#     RetrieveAPIView,
#     UpdateAPIView,
#     DestroyAPIView
# )

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class ServiceView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ServiceSerializer
    queryset = Services.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    ordering_fields = ["id", "created_at"]
    search_fields = ["title", "category__title"]


# class ServiceView(ViewSet):
#     permission_classes = [IsAdminOrReadOnly]
#     serializer_class = ServiceSerializer
#     queryset = Services.objects.all()

#     def list(self, request, *args, **kwargs):
#         service = Services.objects.all()
#         serialize = self.serializer_class(service, many=True)
#         return Response(serialize.data, status=status.HTTP_200_OK)

#     def create(self, request, *args, **kwargs):
#         serilize = self.serializer_class(data=request.data)
#         serilize.is_valid(raise_exception=True)
#         serilize.save()
#         return Response (serilize.data, status=status.HTTP_201_CREATED)

#     def retrieve(self, request, *args, **kwargs):
#         pk = kwargs['pk']
#         service = get_object_or_404(Services, id=pk)
#         serilize = self.serializer_class(service)
#         return Response (serilize.data, status=status.HTTP_201_CREATED)

#     def update(self, request, *args, **kwargs):
#         pk = kwargs['pk']
#         service = get_object_or_404(Services, id=pk)
#         serilize = self.serializer_class(service, data=request.data)
#         serilize.is_valid(raise_exception=True)
#         serilize.save()
#         return Response (serilize.data, status=status.HTTP_201_CREATED)

#     def destroy(self, request, *args, **kwargs):
#         pk = kwargs['pk']
#         service = get_object_or_404(Services, id=pk)

#         service.delete()
#         return Response ({"message" : "object deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


# class ListServiceView(ListAPIView, CreateAPIView):
#     permission_classes = [IsAdminOrReadOnly]
#     serializer_class = ServiceSerializer
#     queryset = Services.objects.all()


# class DetailServiceView(RetrieveAPIView, UpdateAPIView, DestroyAPIView):

#     permission_classes = [IsAdminOrReadOnly]
#     serializer_class = ServiceSerializer
#     lookup_field = "pk"
#     queryset = Services.objects.filter(status=True)


# class ListServiceView(GenericAPIView, ListModelMixin, CreateModelMixin):

#     permission_classes = [IsAdminOrReadOnly]
#     serializer_class = ServiceSerializer

#     def get_queryset(self, **kwargs):
#         return Services.objects.all()

#     def get(self, request, *args, **kwargs):
#         return super().list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return super().create(request, *args, **kwargs)


# class DetailServiceView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):

#     permission_classes = [IsAdminOrReadOnly]
#     serializer_class = ServiceSerializer
#     lookup_field = "pk"
#     queryset = Services.objects.filter(status=True)

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request,*args, **kwargs)

#     def put(self, request,*args, **kwargs):
#         return self.update(request,*args, **kwargs)

#     def patch(self, request,*args, **kwargs):
#         return self.update(request,*args, **kwargs)

#     def delete(self, request,*args, **kwargs):
#         return self.destroy(request,*args, **kwargs)


# class ListServiceView(GenericAPIView):

#     permission_classes = [IsAdminOrReadOnly]
#     serializer_class = ServiceSerializer

#     def get_queryset(self, **kwargs):
#         return Services.objects.all()

#     def get(self, request):
#         services = self.get_queryset()
#         serilize = self.serializer_class(services, many=True)
#         return Response (serilize.data, status=status.HTTP_200_OK)


#     def post(self, request):
#         serilize = self.serializer_class(data=request.data)
#         serilize.is_valid(raise_exception=True)
#         serilize.save()
#         return Response (serilize.data, status=status.HTTP_201_CREATED)


# class DetailServiceView(GenericAPIView):

#     permission_classes = [IsAdminOrReadOnly]
#     serializer_class = ServiceSerializer

#     def get_queryset(self):
#         pk = self.request.parser_context['kwargs']['pk']
#         return get_object_or_404(Services, id=pk)

#     def get(self, request, **kwargs):
#         service = self.get_queryset()
#         serilize = self.serializer_class(service)
#      #         service = self.get_queryset()
#         serilize = self.serializer_class(service, data=request.data)
#         serilize.is_valid(raise_exception=True)
#         serilize.save()
#         return Response (serilize.data, status=status.HTTP_201_CREATED)   return Response (serilize.data, status=status.HTTP_200_OK)


#     def put(self, request, **kwargs):
#         service = self.get_queryset()
#         serilize = self.serializer_class(service, data=request.data)
#         serilize.is_valid(raise_exception=True)
#         serilize.save()
#         return Response (serilize.data, status=status.HTTP_201_CREATED)

#     def patch(self, request, **kwargs):
#         service = self.get_queryset()
#         serilize = self.serializer_class(service, data=request.data)
#         serilize.is_valid(raise_exception=True)
#         serilize.save()
#         return Response (serilize.data, status=status.HTTP_201_CREATED)

#     def delete(self, request, **kwargs):
#         service = self.get_queryset()
#         service.delete()
#         return Response ({"message" : "object deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

# class ListServiceView(APIView):
#     permission_classes = [IsAdminOrReadOnly]

#     def get(self, request):
#         services = Services.objects.all()
#         serilize = ServiceSerializer(services, many=True)
#         return Response (serilize.data, status=status.HTTP_200_OK)


#     def post(self, request):
#         serilize = ServiceSerializer(data=request.data)
#         serilize.is_valid(raise_exception=True)
#         serilize.save()
#         return Response (serilize.data, status=status.HTTP_201_CREATED)


# class DetailServiceView(APIView):
#     permission_classes = [IsAdminOrReadOnly]

#     def get(self, request, **kwargs):
#         services = get_object_or_404(Services, id=kwargs.get('pk'))
#         serilize = ServiceSerializer(services)
#         return Response (serilize.data, status=status.HTTP_200_OK)


#     def put(self, request, **kwargs):
#         service = get_object_or_404(Services, id=kwargs.get('pk'))
#         serilize = ServiceSerializer(service, data=request.data)
#         serilize.is_valid(raise_exception=True)
#         serilize.save()
#         return Response (serilize.data, status=status.HTTP_201_CREATED)

#     def patch(self, request, **kwargs):
#         service = get_object_or_404(Services, id=kwargs.get('pk'))
#         serilize = ServiceSerializer(service, data=request.data)
#         serilize.is_valid(raise_exception=True)
#         serilize.save()
#         return Response (serilize.data, status=status.HTTP_201_CREATED)

#     def delete(self, request, **kwargs):
#         service = get_object_or_404(Services, id=kwargs.get('pk'))
#         service.delete()
#         return Response ({"message" : "object deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


# @api_view(["GET", "POST"])
# @permission_classes([IsAdminOrReadOnly])
# def all_services(request):
#     if request.method == "GET":
#         services = Services.objects.all()
#         serilize = ServiceSerializer(services, many=True)
#         return Response (serilize.data, status=status.HTTP_200_OK)

#     elif request.method == "POST":
#             serilize = ServiceSerializer(data=request.data)
#             if serilize.is_valid():
#                 serilize.save()
#                 return Response (serilize.data, status=status.HTTP_201_CREATED)
#             else:
#                 return Response (serilize.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(["GET", "PUT", "DELETE", "PATCH"])
# def single_services (request, id):
#         services = get_object_or_404(Services, id=id)
#         if request.method == "GET":
#             serialize = ServiceSerializer(services)
#             return Response (serialize.data, status=status.HTTP_200_OK)
#         elif request.method == "PUT":
#              serialize = ServiceSerializer(services, data=request.data)
#              serialize.is_valid(raise_exception=True)
#              #if serialize.is_valid():
#              serialize.save()
#              return Response (serialize.data, status=status.HTTP_202_ACCEPTED)
#         elif request.method == "PATCH":
#              serialize = ServiceSerializer(services, data=request.data)
#              serialize.is_valid(raise_exception=True)
#              #if serialize.is_valid():
#              serialize.save()
#              return Response (serialize.data, status=status.HTTP_202_ACCEPTED)
#         elif request.method == "DELETE":
#              services.delete()
#              return Response ({"message" : "object deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


# @api_view(["GET", "POST"])
# @permission_classes([IsAuthenticatedOrReadOnly])
# def all_comments(request):
#     if request.method == "GET":
#         comments = Comments.objects.all()
#         serilize = CommentSerializer(comments, many=True)
#         return Response (serilize.data, status=status.HTTP_200_OK)

#     elif request.method == "POST":
#         serilize = CommentSerializer(data=request.data)
#         if serilize.is_valid():
#             serilize.save()
#             return Response (serilize.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response (serilize.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(["GET", "DELETE", "PATCH"])
# @permission_classes([IsAuthenticatedOrReadOnly])
# def single_comment (request, id):
#         comment = get_object_or_404(Comments, id=id)
#         if request.method == "GET":
#             serialize = CommentSerializer(comment)
#             return Response (serialize.data, status=status.HTTP_200_OK)
#         elif request.method == "PATCH":
#              if request.user.id == comment.name.id :
#                 serialize = CommentSerializer(comment, data=request.data)
#                 serialize.is_valid(raise_exception=True)
#                 #if serialize.is_valid():
#                 serialize.save()
#                 return Response (serialize.data, status=status.HTTP_202_ACCEPTED)
#              else:
#                  return Response ({"message" : "this object is not for you"}, status=status.HTTP_400_BAD_REQUEST)

#         elif request.method == "DELETE":
#              if request.user.id == comment.name.id :
#                 comment.delete()
#                 return Response ({"message" : "object deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
#              else:
#                  return Response ({"message" : "this object is not for you"}, status=status.HTTP_400_BAD_REQUEST)
