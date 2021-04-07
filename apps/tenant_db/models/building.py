from django.db import models
from .gsheets import Gsheets_Building


class Building(models.Model):
    street_number = models.CharField(max_length=30)
    street_name = models.CharField(max_length=30)
    postal_code = models.CharField(max_length=6)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    source = models.OneToOneField(Gsheets_Building, on_delete=models.CASCADE, null=True, unique=True)
