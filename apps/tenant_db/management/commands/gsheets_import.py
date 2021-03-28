from apps.tenant_db import models

from django_cron import CronJobBase, Schedule
from django.core.management.base import BaseCommand, CommandError
from phonenumber_field.phonenumber import to_python
from django.db.models import Value as V
from django.db.models.functions import Concat

def pull_sheets():
    models.Gsheets_Contact.pull_sheet()
    models.Gsheets_Building.pull_sheet()

class Command(BaseCommand):
    help = "Run gsheets import, if configured"

    def sync_buildings(self):
        for gsheets_building in models.Gsheets_Building.objects.all():
            if gsheets_building.Street_Number == "":
                continue
            print(f"Syncing {gsheets_building.Street_Number} {gsheets_building.Street_Name}")
            try: 
                
                building = models.Building.objects.get(source__pk=gsheets_building.id)
                print(f"Existing entry for {gsheets_building.Street_Number} {gsheets_building.Street_Name} found. Updating in place.")

                building.street_number = gsheets_building.Street_Number
                building.street_name = gsheets_building.Street_Name
                building.postal_code = gsheets_building.Postal_Code.replace(" ", "")
                building.save()

            except Exception as e:
                print(f"No entry for {gsheets_building.Street_Number} {gsheets_building.Street_Name} found. Creating one.")
                building = models.Building.objects.create(
                    street_number = gsheets_building.Street_Number,
                    street_name = gsheets_building.Street_Name,
                    postal_code = gsheets_building.Postal_Code.replace(" ", ""),
                    source = gsheets_building
                )

        for building in models.Building.objects.filter(source__isnull=False):
            if not building.source in models.Gsheets_Building.objects.all():
                print(f"Deleting building {building.street_number} {building.street_name}")
                building.delete()

    def sync_contacts(self):
        for gsheets_contact in models.Gsheets_Contact.objects.all():
            if gsheets_contact.First_Name == "" and gsheets_contact.Last_Name == "" and gsheets_contact.Unit_Number == "":
                continue

            print(f"Syncing {gsheets_contact.First_Name} {gsheets_contact.Last_Name}")
            try: 
                contact = models.Contact.objects.get(source__pk=gsheets_contact.id)
                print(f"Existing entry for {gsheets_contact.First_Name} {gsheets_contact.Last_Name} found. Updating in place.")
                contact.first_name = gsheets_contact.First_Name
                contact.last_name = gsheets_contact.Last_Name
                contact.phone_number = gsheets_contact.Phone_Number
                contact.email_address = gsheets_contact.Email_Address
                contact.unit_number = gsheets_contact.Unit_Number
                contact.notes = gsheets_contact.Notes

                try: 
                    building = models.Building.objects.annotate(
                        address=Concat('street_number', V(' '), 'street_name')
                    ).get(address=gsheets_contact.Address)
                    contact.address = building

                    organizer = models.Organizer.objects.annotate(
                        name=Concat('first_name', V(' '), 'last_name')
                    ).get(name=gsheets_contact.Organizer)
                    contact.organizer = organizer
                except:
                    pass

                contact.save()
            except Exception as e:
                print(e)
                print(f"No entry for {gsheets_contact.First_Name} {gsheets_contact.Last_Name} found. Creating one.")

                contact = models.Contact.objects.create(
                    first_name = gsheets_contact.First_Name,
                    last_name = gsheets_contact.Last_Name,
                    phone_number = gsheets_contact.Phone_Number,
                    email_address = gsheets_contact.Email_Address,
                    unit_number = gsheets_contact.Unit_Number,
                    source = gsheets_contact
                )

                try: 
                    building = models.Building.objects.annotate(
                        address=Concat('street_number', V(' '), 'street_name')
                    ).get(address=gsheets_contact.Address)
                    contact.address = building
                    contact.save()
                except:
                    pass

        for contact in models.Contact.objects.filter(source__isnull=False):
            if not contact.source in models.Gsheets_Contact.objects.all():
                print(f"Deleting contact {contact.street_number} {contact.street_name}")
                contact.delete()

    
    def handle(self, *args, **options):
        #pull_sheets()
        # Order here does matter in order to resolve foreign keys
        self.sync_buildings()
        self.sync_contacts()

