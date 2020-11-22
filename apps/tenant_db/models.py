from django.db import models
from django.core.validators import EmailValidator

class Building(models.Model):
    street_number = models.CharField(max_length=30)
    street_name = models.CharField(max_length=30)
    postal_code = models.CharField(max_length=6)

class Contact(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.ForeignKey(Building, on_delete=models.CASCADE, null=True)
    email_address = models.CharField(max_length=30, validators=[EmailValidator])
    unit_number = models.CharField(max_length=4)
