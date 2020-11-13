from django.db import models


class Building_Address(models.Model):
    street_number = models.CharField(max_length=30)
    street_name = models.CharField(max_length=30)
    postal_code - models.CharField(max_length=30)
    
class Household_Address(models.Model):
    building_address = models.ForeignKey(Building_Address, on_delete=models.CASCADE)
    unit_number = models.CharField(max_length=4)

class Contact(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.ForeignKey(Household_Address, on_delete=models.CASCADE)

class Building(models.Model):
    address = models.ForeignKey(Building_Address, on_delete=models.CASCADE)
