from apps.tenant_db import models
from rest_framework import serializers

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Contact
        fields = ['id', 'first_name', 'last_name', 'email_address']

    def create(self, validated_data):
        return models.Contact.objects.create(**validated_data)

class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Building
        fields = '__all__'

    def create(self, validated_data):
        return models.Building.objects.create(**validated_data)
