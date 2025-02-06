from rest_framework import serializers
from services.models import Services



class ServiceSerializer(serializers.ModelSerializer):
    # title = serializers.CharField()
    # status = serializers.BooleanField()

    class Meta:
        model = Services
        fields = ["title", "content", "category", "status"]