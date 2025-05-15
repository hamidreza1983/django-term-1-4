from rest_framework.viewsets import ModelViewSet
from .serializer import ContactUsSerializer
from django.views.decorators.csrf import csrf_exempt


#@csrf_exempt
class ContactView(ModelViewSet):
    serializer_class = ContactUsSerializer
