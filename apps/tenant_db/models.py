from django.db import models
from django.core.validators import EmailValidator

class Building(models.Model):
    street_number = models.CharField(max_length=30)
    street_name = models.CharField(max_length=30)
    postal_code = models.CharField(max_length=6)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Organizer(models.Model):
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Contact(models.Model):
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)

    email_address = models.EmailField(max_length=254, null=True)
    phone_number = models.CharField(
        max_length=30
    )

    address = models.ForeignKey(Building, on_delete=models.CASCADE, null=True)
    unit_number = models.CharField(max_length=4, null=True)

    organizer = models.ForeignKey(Organizer, on_delete=models.CASCADE, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Do_Not_Knock(models.Model):
    address = models.ForeignKey(Building, on_delete=models.CASCADE, null=True)
    unit_number = models.CharField(max_length=4, null=True)
    notes = models.CharField(max_length=120, null=True)
