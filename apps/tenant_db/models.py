from django.db import models
from django.core.validators import EmailValidator
from gsheets import mixins
from phonenumber_field.modelfields import PhoneNumberField

class CallResult(models.TextChoices):
    DO_NOT_CALL = 'DNC'
    NOT_AVAILABLE = 'N/A'
    MESSAGE = 'MSG'
    YES = 'Y'
    MAYBE = 'M'
    NO = 'N'

class CallResult(models.TextChoices):
    DO_NOT_CALL = 'DNC'
    NOT_AVAILABLE = 'N/A'
    MESSAGE = 'MSG'
    YES = 'Y'
    MAYBE = 'M'
    NO = 'N'

class Gsheets_Contact(mixins.SheetPullableMixin, models.Model):
    spreadsheet_id = '1bjOqj3InBdOgucpujo3MknNfdQWQfjM8g1HH6ewmI0M'
    sheet_name = 'Contacts'
    First_Name = models.TextField()
    Last_Name = models.TextField()
    Address = models.TextField()
    Unit_Number = models.TextField()
    Phone_Number = models.TextField()
    Email_Address = models.TextField()
    Notes = models.TextField()
    Organizer = models.TextField()
    Entered_By = models.TextField()

class Gsheets_Building(mixins.SheetPullableMixin, models.Model):
    spreadsheet_id = '1bjOqj3InBdOgucpujo3MknNfdQWQfjM8g1HH6ewmI0M'
    sheet_name = 'Turf'
    Street_Number = models.TextField()
    Street_Name = models.TextField()
    Floors = models.TextField()
    Thirteenth_Floor = models.TextField()
    City = models.TextField()
    Postal_Code = models.TextField()
    Owner = models.TextField()
    Prominent_Issues = models.TextField()
    Organizer = models.TextField()

class Building(models.Model):
    street_number = models.CharField(max_length=30)
    street_name = models.CharField(max_length=30)
    postal_code = models.CharField(max_length=6)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    source = models.OneToOneField(Gsheets_Building, on_delete=models.CASCADE, null=True, unique=True)


class Organizer(models.Model):
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


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
