# TODO: Add to its own app

from django.db import models
from gsheets import mixins


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
