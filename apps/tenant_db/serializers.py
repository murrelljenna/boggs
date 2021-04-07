from apps.tenant_db import models
from rest_framework import serializers

class CallEffortSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CallEffort
        fields = "__all__"

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Activity
        fields = "__all__"

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

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Event
        fields = "__all__"
