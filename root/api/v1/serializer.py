from rest_framework import serializers
from root.models import ContactUs



class ContactUsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContactUs
        fields = "__all__"

