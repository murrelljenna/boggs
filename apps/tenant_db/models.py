from django.db import models
from django.core.validators import EmailValidator

class CallResult(models.TextChoices):
    DO_NOT_CALL = 'DNC'
    NOT_AVAILABLE = 'N/A'
    MESSAGE = 'MSG'
    YES = 'Y'
    MAYBE = 'M'
    NO = 'N'

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

class Event(models.Model):
    name = models.CharField(max_length=30, null=False)
    location = models.CharField(max_length=30, null=True)
    description = models.CharField(max_length=30, null=True)

class Attendance(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, null=False)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=False)
    result = models.CharField(
        max_length=3,
        choices=CallResult.choices,
        default=CallResult.NOT_AVAILABLE,
    )

class Do_Not_Knock(models.Model):
    address = models.ForeignKey(Building, on_delete=models.CASCADE, null=True)
    unit_number = models.CharField(max_length=4, null=True)
    notes = models.CharField(max_length=120, null=True)
