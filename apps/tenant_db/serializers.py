from apps.tenant_db import models
from rest_framework import serializers
from django.contrib.auth.models import User


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Contact
        fields = "__all__"


class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Building
        fields = "__all__"


class OrganizerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Organizer
        fields = "__all__"

class dnkSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Do_Not_Knock
        fields = "__all__"
