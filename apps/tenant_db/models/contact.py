from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from .building import Building
from .organizer import Organizer

from .gsheets import Gsheets_Contact


class Contact(models.Model):
    first_name = models.CharField(max_length=120, null=True)
    last_name = models.CharField(max_length=120, null=True)

    email_address = models.EmailField(max_length=254, null=True)
    phone_number = PhoneNumberField(
        blank=True
    )

    address = models.ForeignKey(Building, on_delete=models.CASCADE, null=True)
    unit_number = models.CharField(max_length=4, null=True)
    notes = models.TextField()

    organizer = models.ForeignKey(Organizer, on_delete=models.CASCADE, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    source = models.OneToOneField(Gsheets_Contact, on_delete=models.CASCADE, null=True, unique=True)
