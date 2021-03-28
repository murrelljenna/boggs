"""tenant_crm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework import generics
from django.conf.urls import include
from apps.tenant_db import models, serializers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
import django_filters.rest_framework
from django_filters.rest_framework import DjangoFilterBackend
import gsheets as gsheets

class AttendanceListCreateAPIView(generics.ListCreateAPIView):
    filter_backends = [DjangoFilterBackend]
    filterset_fields=['event']

urlpatterns = [
    path("admin/", admin.site.urls),
    path("token-auth/", TokenObtainPairView.as_view()),
    path("token-refresh/", TokenRefreshView.as_view()),
    path('', include('gsheets.urls')),
    # path("", include("apps.tenant_db.urls")),
    # Contacts
    path(
        "contacts/",
        generics.ListCreateAPIView.as_view(
            queryset=models.Contact.objects.all(),
            serializer_class=serializers.ContactSerializer,
        ),
        name="contacts",
    ),
    path(
        "contacts/<int:pk>/",
        generics.RetrieveUpdateDestroyAPIView.as_view(
            queryset=models.Contact.objects.all(),
            serializer_class=serializers.ContactSerializer,
        ),
        name="contacts_detail",
    ),
    # Buildings
    path(
        "buildings/",
        generics.ListCreateAPIView.as_view(
            queryset=models.Building.objects.all(),
            serializer_class=serializers.BuildingSerializer,
        ),
        name="buildings/",
    ),
    path(
        "buildings/<int:pk>/",
        generics.RetrieveUpdateDestroyAPIView.as_view(
            queryset=models.Building.objects.all(),
            serializer_class=serializers.BuildingSerializer,
        ),
        name="buildings_detail",
    ),
    # Organizer
    path(
        "organizers/",
        generics.ListCreateAPIView.as_view(
            queryset=models.Organizer.objects.all(),
            serializer_class=serializers.OrganizerSerializer,
        ),
        name="Organizers",
    ),
    path(
        "organizers/<int:pk>/",
        generics.RetrieveUpdateDestroyAPIView.as_view(
            queryset=models.Organizer.objects.all(),
            serializer_class=serializers.OrganizerSerializer,
        ),
        name="organizers_detail",
    ),

    # Event
    path(
        "events/",
        generics.ListCreateAPIView.as_view(
            queryset=models.Event.objects.all(),
            serializer_class=serializers.EventSerializer,
        ),
        name="events",
    ),
    path(
        "events/<int:pk>/",
        generics.RetrieveUpdateDestroyAPIView.as_view(
            queryset=models.Event.objects.all(),
            serializer_class=serializers.EventSerializer,
        ),
        name="events_detail",
    ),
    # Event
    path(
        "attendances",
        AttendanceListCreateAPIView.as_view(
            queryset=models.Attendance.objects.all(),
            serializer_class=serializers.AttendanceSerializer,
            filter_backends=[django_filters.rest_framework.DjangoFilterBackend],
        ),
        name="attendances",
    ),
    path(
        "attendances/<int:pk>/",
        generics.RetrieveUpdateDestroyAPIView.as_view(
            queryset=models.Attendance.objects.all(),
            serializer_class=serializers.AttendanceSerializer,
        ),
        name="attendances_detail",
    ),
    # Do Not Knock
    path(
        "dnk/",
        generics.ListCreateAPIView.as_view(
            queryset=models.Do_Not_Knock.objects.all(),
            serializer_class=serializers.dnkSerializer,
        ),
        name="dnk",
    ),
    path(
        "dnk/<int:pk>/",
        generics.RetrieveUpdateDestroyAPIView.as_view(
            queryset=models.Do_Not_Knock.objects.all(),
            serializer_class=serializers.dnkSerializer,
        ),
        name="dnk_detail",
    ),
]
