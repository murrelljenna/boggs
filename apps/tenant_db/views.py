import io

from django.shortcuts import render, get_object_or_404
from django.core import serializers
from django.http import JsonResponse
from apps.tenant_db import models
from apps.tenant_db.serializers import ContactSerializer
from apps.tenant_db.serializers import BuildingSerializer

from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

class ContactViewSet(viewsets.ViewSet):
    queryset = models.Contact.objects.all()

    def get_queryset(self):
        return models.Contact.objects.all()

    def list(self, request):
        return Response(
		serializers.serialize("json", self.get_queryset()), 
		headers={
			'Access-Control-Allow-Origin': 'http://localhost:3000',
		}
	)

    def retrieve(self, request, pk):
        return Response(serializers.serialize("json", get_object_or_404(self.get_queryset(), id=pk)))

    def create(self, request):
        data = JSONParser().parse(io.BytesIO(request.body))
        serializer = ContactSerializer(data=data)
        if (serializer.is_valid()):
            contact = serializer.save()
            return Response(ContactSerializer(contact).data, status=201)
        else:
            return Response(status=400)

    def partial_update(self, request, pk=None):
        data = JSONParser().parse(io.BytesIO(request.body))
        test = self.get_queryset().filter(id = pk).update(**data)
        
        return Response(200)

    def destroy(self, request, pk=None):
        get_object_or_404(self.get_queryset(), id=pk).delete();
        return Response(status=204)    

class BuildingViewSet(viewsets.ViewSet):
    queryset = models.Building.objects.all()

    def get_queryset(self):
        return models.Building.objects.all()

    def list(self, request):
        return Response(serializers.serialize("json", self.get_queryset()))

    def retrieve(self, request, pk=None):
        bAddr = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = BuildingSerializer(bAddr)
        return Response(serializer.data)

    def create(self, request):
        data = JSONParser().parse(io.BytesIO(request.body))
        serializer = BuildingSerializer(data=data)
        if (serializer.is_valid()):
            gAddr = serializer.save()
        return Response(serializer.data)

